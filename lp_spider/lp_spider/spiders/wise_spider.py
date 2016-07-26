#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################

"""
    File: wise_spider.py
Author: root(root@baidu.com)
    Date: 2016/07/20 19:41:27
    """
import scrapy
import os
from scrapy.selector import HtmlXPathSelector
import hashlib
import urllib

data_path = "/notebooks/lp_output/"
input_file = data_path + "/all_wise_url.res"
urls = set()
dic_url = {}

with open(input_file, 'r') as fin:
    for line in fin:
        vals = line.strip().split('\t')
        url_sign = vals[0]
        url = vals[1]
        urls.add(url)
        dic_url[url] = url_sign

def get_str(list_in, encoding='utf8'):
    """
    """
    out_str = ''
    for i in list_in: 
        if i != "":
            out_str += i.strip().encode(encoding) + " "
    return out_str.strip()


class WiseSpider(scrapy.spiders.Spider):

    name = "wise"
    start_urls = list(urls)

    def parse(self, response):
        redirect_tag = False
        if "redirect_urls" in response.meta:
            redirect_tag = True
            url_raw = response.meta["redirect_urls"][0]
            url = urllib.unquote(url_raw)
        else:
            url_raw = response.request.url
            url = urllib.unquote(url_raw)
        output_path = data_path + '/wise/'
        output_title_path = output_path + '/title/'
        output_desc_path = output_path + '/desc/'
        output_important_path = output_path + '/important/'
        os.system("mkdir -p %s" % (output_title_path))
        os.system("mkdir -p %s" % (output_desc_path))
        os.system("mkdir -p %s" % (output_important_path))
        hash_str = hashlib.md5() ## can't use global variable...
        hash_str.update(url)
        filename_title = output_title_path + hash_str.hexdigest()
        filename_desc = output_desc_path + hash_str.hexdigest()
        filename_important = output_important_path + hash_str.hexdigest()
        hxs = HtmlXPathSelector(response)
        title = hxs.select('/html/head/title/text()')
        a_text = hxs.select('//a/text()')
        important_text = hxs.select('//b/text()')
        
        with open(filename_title, 'wb') as fout_title, \
            open(filename_desc, 'wb') as fout_desc, \
            open(filename_important, 'wb') as fout_important:
            title_str = get_str(title.extract(), encoding="utf8")
            a_text_str = get_str(a_text.extract(), encoding="utf8")
            important_text_str = get_str(important_text.extract(), encoding="utf8")
            fout_title.write(title_str + '\n')
            fout_desc.write(a_text_str + '\n')
            fout_important.write(important_text_str + '\n')

