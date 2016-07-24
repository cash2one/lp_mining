#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################

"""
    File: pc_spider.py
Author: root(root@baidu.com)
    Date: 2016/07/20 19:41:27
    """
import scrapy
import hashlib

input_file = "/root/daiwk_lp/lp_mining/lp_spider/all_pc_url.res"
urls = set()

with open(input_file, 'r') as fin:
    for line in fin:
        vals = line.strip().split('\t')
        url_sign = vals[0]
        url = vals[1]
        urls.add(url)

class PcSpider(scrapy.spiders.Spider):

    name = "pc"
    #allowed_domains = ["pc.org", "baidu.com"]
    start_urls = list(urls)

    def parse(self, response):
        output_path = '/root/daiwk_lp/lp_mining/output/'
        #filename = output_path + response.url.split("/")[-2]
        hash_str = hashlib.md5() ## ²»ÄÜ·ÅÈ«¾ÖµÄ£ÒªÃ¿´ÎÊ¹ÓÃÉùÃ÷¡£¡£²»È»update»áÔÚÉÏÒ»´ÎµÄ»ù´¡ÉÏ¸Ä¡£¡£
        hash_str.update(str(response.url))
        filename = output_path + hash_str.hexdigest()
        with open(filename, 'wb') as f:
            f.write(response.url+'\n')
            f.write(response.body)

