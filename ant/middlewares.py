import datetime
import os, re, sys, md5, json, socket, urllib
import spiders.ant_spider, scl
import lxml.etree as etree

from ant.spiders.ant_spider import AntSpider
from ant.items import AntItem
from scrapy.utils.url import escape_ajax, safe_url_string
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from scrapy import log

from urlparse import urlparse, urljoin


fetchlinks = { }


class ProxyMiddleware(object):
  def process_request(self, request, spider):
    if socket.gethostname() == 'broom.ashmanov.com':
        request.meta['proxy'] = "http://127.0.0.1:8080"
    else:
        request.meta['proxy'] = "http://plow.ashmanov.com:8080"


class DownloaderMiddleware(object):
  myScl = scl.Scl()
  def process_request(self, request, spider):
    fh = AntSpider.fh;

  def escape(self, string):
    string = string.replace('"', '\\"')
    string = string.replace('\r', ' ')
    string = string.replace('\n', ' ')
    string = string.replace('\t', ' ')
    return string

  def parse_title(self, response):
    sel = response.xpath('//ul/li')
    title = response.selector.xpath('/html/head/title/text()').extract()
    res = ''
    for phrase in title:
      '''if response.encoding != 'utf-8':
        try:
          phrase = phrase.decode(response.encoding).encode('utf-8')
        except UnicodeDecodeError as e:
          print 'Title:', e, response.encoding'''
      res += phrase
    return res

  def get_metacats_termin(self, jsonData, url):
    listMetaCats = { }
    try:
      objJson = json.loads(jsonData, encoding="utf-8")
      cats = objJson["cats"]
      metaCats = objJson["META_CATS"]
      if metaCats:
        terms = objJson["terms"]
        for key in metaCats:
          matchCats = self.myScl.match(key, cats);
          for matchCat in matchCats:
            listMetaCats[key] = []
            rx = r'^' + matchCat
            for term in terms:
              if re.match(rx, term[0]):
                listMetaCats[key].append(term[1])
    except Exception as e:
      print 'Exception in parse JSON: ', e, ': ', url
    return listMetaCats

  def get_metacats_snippets(self, jsonData, url):
    listMetaCats = { }
    try:
      objJson = json.loads(jsonData, encoding="utf-8")
      snippets = objJson["snippets"]
      for cat in objJson["cats"]:
        for snippet in snippets:
          if snippet["r"].find(cat) == 0:
            metaCats = self.myScl.match(cats=(cat,))
            for metacat in metaCats:
              if metacat in listMetaCats:
                listMetaCats[metacat] += snippet["s"]
              else:
                listMetaCats[metacat] = snippet["s"]
    except Exception as e:
      print 'Exception in parse JSON:', e, url
    return listMetaCats

  def get_md5(self, url):
    urlHash = md5.new()
    urlHash.update(url)
    return urlHash.hexdigest()

  def _iter_links(self, document):
    for el in document.iter(etree.Element):
      attribs = el.attrib
      for attrib in attribs:
        yield (el, attrib, attribs[attrib])

  def _match_element(self, tag, attrib):
    tag = tag.upper()
    attrib = attrib.upper()
    if tag in ['LINK', 'A', 'AREA', 'SCRIPT', 'IMG', 'IFRAME', 'FRAME', 'EMBED'] \
      and attrib in ['HREF', 'SRC']:
      return True
    elif tag in ['APPLET'] and attrib in ['CODE', 'ARCHIVE', 'CODEBASE']:
      return True
    elif tag in ['FORM'] and attrib in ['ACTION']:
      return True
    else:
      return False

  def fetch_links(self, document, base_url):
    global fetchlinks
    try:
      for el, attr, attr_val in self._iter_links(document):
        if self._match_element(el.tag, attr):
          if attr_val.find('http://') > 0:
            url = attr_val[attr_val.find('http://'):]
          elif attr_val.find('https://') > 0:
            url = attr_val[attr_val.find('https://'):]
          elif attr_val[:2] == '//':
            url = base_url[:base_url.find('://') + 1] + attr_val
          else:
            url = urljoin(base_url, attr_val)
          _url = str(url)
          #if isinstance(url, unicode):
            #url = url.encode(response_encoding, errors='ignore')
          url = escape_ajax(safe_url_string(url))
          n = url.find('#')
          if n != -1:
            url = url[:n]
          urlmd5 = self.get_md5(url)
          _tag = str(el.tag)
          _attr = str(attr if attr is not None else '')
          _txt = str(el.text if el.text is not None else '')
          fetchlinks[urlmd5] = (_tag, _attr, _txt, _url)
    except AttributeError as e:
      print 'Exception: ', e, base_url

  def process_response(self, request, response, spider):
    fh = AntSpider.fh
    referer = request.headers.get('Referer')
    http_status = response.status
    body = response.body
    url = response.url
    redirect_urls = request.meta.get('redirect_urls', [])
    origin_url = redirect_urls[0] if redirect_urls else url
    urlmd5 = self.get_md5(origin_url)
    taginfo = fetchlinks.get(urlmd5)
    if taginfo is None and origin_url[-1] == '/':
      origin_url = origin_url[:len(origin_url)-1]
      urlmd5 = self.get_md5(origin_url)
      taginfo = fetchlinks.get(urlmd5)
    #print 'process_response:', origin_url
    section = spider.section
    title = ''
    listMetaCats = { }
    anchor = ''
    tag = ''
    jsonData = ''
    contentType = response.headers.get('Content-Type')
    contentTypeIsText = contentType.find('text/html') != -1 if contentType else False
    contentTypeIsImage = contentType.find('image') != -1 if contentType else False
    if contentTypeIsText:
        self.fetch_links(Selector(text=body)._root, origin_url)
        startBody = body.find("<!-- # webfilter.parameters")
        if startBody != -1:
          endBody = body.find("// # webfilter.parameters -->")
          if endBody != -1:
            jsonData = body[startBody+28 : endBody-1]
            #listMetaCats = self.get_metacats_snippets(jsonData, url)
            listMetaCats = self.get_metacats_termin(jsonData, origin_url)
    if http_status >= 200 and http_status < 300:
      if contentTypeIsText:
        title = self.escape(self.parse_title(response))
        title = re.sub(r'\r?\n', ' ', title)
        title = re.sub(r'^\s*|\s*$', '', title)
      elif contentTypeIsImage:
        pass
    elif http_status >= 300 and http_status < 400:
        pass
    elif http_status >= 400 and http_status < 600:
      if taginfo is not None:
        tag  = taginfo[0]
        attr = taginfo[1]
        text = taginfo[2]
        url  = taginfo[3]
        if tag == 'img' and attr == 'alt':
          anchor = self.escape(attr)
        else:
          anchor = self.escape(text)
      else:
        print 'Tag not find for:', origin_url
    else:
      pass
    referer = '' if referer is None else referer
    line  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t"
    line += str(http_status)  + "\t"
    line += origin_url        + "\t"
    line += "SECTION:" + "\"" + section     + "\"" + "\t"
    if title:
      line += "TITLE:" + "\"" + title       + "\"" + "\t"
    for metaCats in listMetaCats:
      k = listMetaCats[metaCats]
      s = '|'.join(str(e) for e in k)
      line += "SCL:"   + "\"" + metaCats + ":" + s.encode('utf-8') + "\"" + "\t"
    if anchor:
      line += "ANCHOR:"+ "\"" + anchor      + "\"" + "\t"
    if tag:
      line += "TAG:"   + "\"" + tag         + "\"" + "\t"
    if contentType:
      line += "TYPE:"  + "\"" + contentType + "\"" + "\t"
    if referer:
      line += "REFER:" + "\"" + referer     + "\"" + "\t"
    line += "\n"
    line = line.encode("utf-8", errors="ignore")
    fh.write(line)
    #if taginfo is not None:
      #del spiders.ant_spider.elements[urlmd5]
    return response

  def process_exception(self, request, exception, spider):
    print exception
