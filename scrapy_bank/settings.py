# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_bank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


BOT_NAME = 'scrapy_bank'

SPIDER_MODULES = ['scrapy_bank.spiders']
NEWSPIDER_MODULE = 'scrapy_bank.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_bank (+http://www.yourdomain.com)'
#COOKIES_DEBUG = True
ITEM_PIPELINES = {
}


CONCURRENT_REQUESTS = 50
CONCURRENT_REQUESTS_PER_DOMAIN = 30
DOWNLOADER_MIDDLEWARES = {
    'scrapy_bank.middlewares.EncodeUtf8Response': 100,
    'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': 1000,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    #'scrapy_bank.useragent.RandomUserAgentMiddleware' :400
}

EXTENSIONS = {

}

S3_BUCKET = 'test-skilledup-products/test_upload'
S3_ACCESS_KEY = 'AKIAI4GM7OCYVUHEXZHQ'
S3_SECRET_KEY = '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'
S3_ENDPOINT = 's3-us-west-1.amazonaws.com'


DOWNLOAD_DELAY = 1

DOWNLOADER_CLIENTCONTEXTFACTORY = 'scrapy_bank.contextfactory.CustomClientContextFactory'

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
