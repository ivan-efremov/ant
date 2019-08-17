
from twisted.internet import defer, reactor, protocol
from scrapy.xlib.tx import Agent, ProxyAgent, ResponseDone, \
    HTTPConnectionPool, TCP4ClientEndpoint
from scrapy.http import Headers
from scrapy.core.downloader import webclient as client
from scrapy.core.downloader import Downloader
from scrapy.core.downloader.webclient import _parse
from scrapy.core.downloader.handlers.http11 import *


class AntAgent(object):
  _Agent = Agent
  _ProxyAgent = ProxyAgent
  _TunnelingAgent = TunnelingAgent

  def __init__(self, contextFactory=None, connectTimeout=10, bindAddress=None, pool=None):
    self._contextFactory = contextFactory
    self._connectTimeout = connectTimeout
    self._bindAddress = bindAddress
    self._pool = pool
    self._endpoint = None

  def _get_agent(self, request, timeout):
    bindaddress = request.meta.get('bindaddress') or self._bindAddress
    proxy = request.meta.get('proxy')
    if proxy:
      _, _, proxyHost, proxyPort, proxyParams = _parse(proxy)
      scheme = _parse(request.url)[0]
      omitConnectTunnel = proxyParams.find('noconnect') >= 0
      if scheme == 'https' and not omitConnectTunnel:
        proxyConf = (proxyHost, proxyPort,
                      request.headers.get('Proxy-Authorization', None))
        return self._TunnelingAgent(reactor, proxyConf,
            contextFactory=self._contextFactory, connectTimeout=timeout,
            bindAddress=bindaddress, pool=self._pool)
      else:
        if self._endpoint is None:
          self._endpoint = TCP4ClientEndpoint(reactor, proxyHost, proxyPort,
            timeout=timeout, bindAddress=bindaddress)
        return self._ProxyAgent(self._endpoint, reactor, self._pool)
    return self._Agent(reactor, contextFactory=self._contextFactory,
        connectTimeout=timeout, bindAddress=bindaddress, pool=self._pool)

  def download_request(self, request):
    timeout = request.meta.get('download_timeout') or self._connectTimeout
    agent = self._get_agent(request, timeout)
    url = urldefrag(request.url)[0]
    method = request.method
    headers = TxHeaders(request.headers)
    bodyproducer = _RequestBodyProducer(request.body) if request.body else None
    start_time = time()
    d = agent.request(method, url, headers, bodyproducer)
    d.addCallback(self._cb_latency, request, start_time)
    d.addCallback(self._cb_bodyready, request)
    d.addCallback(self._cb_bodydone, request, url)
    self._timeout_cl = reactor.callLater(timeout, d.cancel)
    d.addBoth(self._cb_timeout, request, url, timeout)
    return d

  def _cb_timeout(self, result, request, url, timeout):
    if self._timeout_cl.active():
      self._timeout_cl.cancel()
      return result
    raise TimeoutError("Getting %s took longer than %s seconds." % (url, timeout))

  def _cb_latency(self, result, request, start_time):
    request.meta['download_latency'] = time() - start_time
    return result

  def _cb_bodyready(self, txresponse, request):
    if txresponse.length == 0:
      return txresponse, '', None
    def _cancel(_):
      txresponse._transport._producer.loseConnection()
    d = defer.Deferred(_cancel)
    txresponse.deliverBody(_ResponseReader(d, txresponse, request))
    return d

  def _cb_bodydone(self, result, request, url):
    txresponse, body, flags = result
    status = int(txresponse.code)
    headers = Headers(txresponse.headers.getAllRawHeaders())
    respcls = responsetypes.from_args(headers=headers, url=url)
    return respcls(url=url, status=status, headers=headers, body=body, flags=flags)


class _ResponseReader(protocol.Protocol):
  def __init__(self, finished, txresponse, request):
    self._finished = finished
    self._txresponse = txresponse
    self._request = request
    self._bodybuf = StringIO()

  def dataReceived(self, bodyBytes):
    self._bodybuf.write(bodyBytes)

  def connectionLost(self, reason):
    if self._finished.called:
      return

    body = self._bodybuf.getvalue()
    if reason.check(ResponseDone):
      self._finished.callback((self._txresponse, body, None))
    elif reason.check(PotentialDataLoss):
      self._finished.callback((self._txresponse, body, ['partial']))
    else:
      self._finished.errback(reason)


class AntDownloadHandler(object):
  def __init__(self, settings):
    self._pool = HTTPConnectionPool(reactor, persistent=True)
    self._pool.maxPersistentPerHost = settings.getint('CONCURRENT_REQUESTS_PER_DOMAIN')
    self._pool._factory.noisy = False
    self._contextFactoryClass = load_object(settings['DOWNLOADER_CLIENTCONTEXTFACTORY'])
    self._contextFactory = self._contextFactoryClass()
    self._agent = AntAgent(contextFactory=self._contextFactory, pool=self._pool)

  def download_request(self, request, spider):
    if self._pool.persistent:
      if not request.headers.get('Connection'):
        request.headers.appendlist('Connection', 'keep-alive')
      proxy = request.meta.get('proxy')
      if proxy and not request.headers.get('Proxy-Connection'):
        request.headers.appendlist('Proxy-Connection', 'keep-alive')
    return self._agent.download_request(request)

  def close(self):
    return self._pool.closeCachedConnections()

