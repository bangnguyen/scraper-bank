import json, re, traceback, time
from langdetect import detect
from scrapy import log
from scrapy import FormRequest, Request, Selector
from scrapy.utils.python import unique
from urlparse import urljoin
import os
import tempfile
import urllib2
import signal
import HTMLParser
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor as lxml
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.html import TextResponse
from scrapy.shell import inspect_response
from scrapy.selector.unified import SelectorList
from scrapy.utils.response import open_in_browser
from scrapy_bank.items import *
from scrapy_bank.utils.html_string import *
from scrapy_bank.linksextractors import RegexLinkExtractor as lrgl
from scrapy_bank.selenium_api import SeleniumApi as slm
from scrapy_bank.selenium_api import *
from scrapy_bank.supportclients.dongabank import *
import pdb

def mapping(value, mappings):
    for k in mappings:
        if contains_ignore_case(value, mappings[k]):
            return k
    return None\


def contains_ignore_case(v, l):
    return v.lower() in [k.lower() for k in l]


def is_existed_in_mapping(value, mappings):
    for k in mappings:
        if contains_ignore_case(value, mappings[k]):
            return True
    return False


def next_fields(fields, level):
    items = {}
    for (k, v) in fields.iteritems():
        if contains(v, 'level'):
            if v['level'] != level:
                fieldsToFields = {}
                if v['level'] in items:
                    fieldsToFields = items[v['level']]
                fieldsToFields[k] = v
                items[v['level']] = fieldsToFields
    return items


def append_to_list(l, data, unique=True):
    l.extend(data) if isinstance(data, list) else l.append(data)
    l = list(set(l)) if unique else l
    return l


"""
return list[selector]
"""


def get_selector(html, field):
    """
    html : Selector or HtmlResponse
    execute the xpath config if existed in field
    """
    try:
        selector = html
        if not ( isinstance(html, Selector) or isinstance(html, SelectorList)):
            selector = Selector(html)
        if contains(field, 'css'):
            selector = selector.css(field['css'])
        if contains(field, 'xpath'):
            #xpath can be a multiple
            selector = xpath(selector, field['xpath'])
        return selector
    except:
        return None


def get_process_type(data):
    if contains(data, 'type'):
        if type(eval(data['type'])) is list:
            return 'list'
        else:
            return 'object'
    elif contains(data, ['xpath', 'css', 're', 'python', 'selenium_function']):
        return 'abstract'
    elif isinstance(data, str):
        return "str"
    elif isinstance(data, unicode):
        return 'unicode'
    elif isinstance(data, int):
        return "int"
    else:
        return None






def view(data):
    if isinstance(data, HtmlResponse) or isinstance(data, TextResponse):
        open_in_browser(data)
    elif isinstance(data, Selector):
        open_in_browser(TextResponse(url="",encoding='utf-8', body=data.extract(), request=None))
    elif isinstance(data, SelectorList):
        content = ""
        for i in data:
            content += "%s <br>" % (i.extract())
        open_in_browser(TextResponse(url="",encoding='utf-8', body=content, request=None))
    else:
        open_in_browser(TextResponse(url="",encoding='utf-8', body=str(data), request=None))












