# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ant'

SPIDER_MODULES = ['ant.spiders']
NEWSPIDER_MODULE = 'ant.spiders'

LOG_LEVEL = 'INFO'
#LOG_FILE = '/var/sitetidy/log/scrapy.log'
#LOG_STDOUT = True

DEPTH_LIMIT = 10

DUPEFILTER_DEBUG = True
DEPTH_STATS_VERBOSE = True
HTTPERROR_ALLOW_ALL = True

DOWNLOAD_HANDLERS = {
    'http': 'ant.downloader.AntDownloadHandler',
    'https': 'ant.downloader.AntDownloadHandler'
}

DOWNLOADER_MIDDLEWARES = {
	'ant.middlewares.ProxyMiddleware': 100,
	'ant.middlewares.DownloaderMiddleware': 101
}

ITEM_PIPELINES = {
    'ant.pipelines.AntPipeline': 200
}

#CONCURRENT_ITEMS = 1
CONCURRENT_REQUESTS = 4
#CONCURRENT_REQUESTS_PER_DOMAIN = 1

#SPIDER_MIDDLEWARES = {
#    'scrapy.contrib.spidermiddleware.DepthMiddleware': None
#}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'

EXTENSIONS = {
    'scrapy.contrib.closespider.CloseSpider': 500
}

#CLOSESPIDER_PAGECOUNT = 5000
#№CLOSESPIDER_TIMEOUT = 3600
