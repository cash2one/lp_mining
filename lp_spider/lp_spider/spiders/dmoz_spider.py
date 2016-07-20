#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################

"""
    File: dmoz_spider.py
Author: root(root@baidu.com)
    Date: 2016/07/20 19:41:27
    """
import scrapy

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org", "baidu.com"]
    start_urls = [
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.baidu.com/", 
    "http://www.jb51.net/article/57183.htm", 
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

