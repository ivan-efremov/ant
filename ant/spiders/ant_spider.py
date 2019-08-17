import scrapy
import re, sys, codecs, copy, md5, os, stat, urllib
import lxml.etree as etree
import threading

from scrapy.link import Link
from scrapy.http import Request
from scrapy.utils.python import unique as unique_list, str_to_unicode
from scrapy.utils.url import escape_ajax, safe_url_string
from scrapy.utils.project import get_project_settings
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.settings.deprecated import check_deprecated_settings
from scrapy import log

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from urlparse import urlparse, urljoin
from subprocess import *


XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"

_collect_string_content = etree.XPath("string()")

def _nons(tag):
  if isinstance(tag, basestring):
    if tag[0] == '{' and tag[1:len(XHTML_NAMESPACE)+1] == XHTML_NAMESPACE:
      return tag.split('}')[-1]
  return tag


class MyLinkExtractor(LinkExtractor):
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

  def _extract_links(self, selector, response_url, response_encoding, base_url):
    global elements
    links = []
    try:
      for el, attr, attr_val in self._iter_links(selector._root):
        if self._match_element(el.tag, attr):
          if attr_val.find('http://') > 0:
            url = attr_val[attr_val.find('http://'):]
          elif attr_val.find('https://') > 0:
            url = attr_val[attr_val.find('https://'):]
          elif attr_val[:2] == '//':
            url = base_url[:base_url.find('://') + 1] + attr_val
          else:
            url = urljoin(base_url, attr_val)
          #if isinstance(url, unicode):
            #url = url.encode(response_encoding, errors='ignore')
          url = escape_ajax(safe_url_string(url))
          n = url.find('#')
          if n != -1:
            url = url[:n]
          link = Link(url, _collect_string_content(el) or u'',
            nofollow=True if el.get('rel') == 'nofollow' else False)
          links.append(link)
    except AttributeError as e:
      print 'Exception: ', e, base_url
    return unique_list(links, key=lambda link: link.url)


def processValue(value):
  print 'TEST: ', value
  return None


class AntSpider(CrawlSpider):
  name = "ant"

  def __init__(self, filename = 'rubric.txt', domain = 'ashmanov.com', fmode = 'w', section = "", outdir = ".", *a, **kw):
    super(AntSpider, self).__init__(*a, **kw)
    dispatcher.connect(self.spider_closed, signals.spider_closed)
    settings = get_project_settings()
    check_deprecated_settings(settings)
    reload(sys)
    sys.setdefaultencoding("UTF-8")
    start_url = domain
    if not re.match(r'^https?://', start_url):
      start_url = 'http://' + start_url
    self.start_urls = [ start_url ]
    parsed_uri = urlparse(start_url)
    domain = parsed_uri.netloc
    self.allowed_domains = [ domain ]
    '''self.rules = (
      Rule(
        LxmlLinkExtractor(
          allow='https?://(www\.)?' + re.sub(r'\.', '\.', domain) + '/',
          deny_extensions=(),
          tags=('a', 'area'),
          attrs=('href',),
          canonicalize=False,
        )
      ),
    )'''
    self.rules = (
      Rule(
        MyLinkExtractor(
          allow = 'https?://(www\.)?' + re.sub( r'\.', '\.', domain ) + '/',
          deny_extensions=(),
          tags=(),
          attrs=(),
          canonicalize=False,
        )
      ),
    )
    self._compile_rules()
    if outdir[-1] != '/':
      outdir += '/'
    filename = outdir + filename + '.' + section
    AntSpider.fh = codecs.open(filename, fmode)
    AntSpider.cnt = 0
    AntSpider.s_start_urls = self.start_urls
    AntSpider.section = section
    os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IWGRP)

  def __del__(self):
    print 'goodbye!'
    AntSpider.fh.close()

  def spider_closed (self):
    try:
      check_call('/usr/bin/perl /opt/sitetidy/scrapy/bin/add_report_task.pl ' + self.start_urls[0], shell=True)
    except CalledProcessError as e:
      print 'Call error:', e
