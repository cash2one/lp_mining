#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: gen_md5.py
Author: root(root@baidu.com)
Date: 2016/07/24 20:45:53
"""
import sys
import hashlib


flag = sys.argv[1]
input_file = "/root/daiwk_lp/lp_mining/lp_spider/all_%s_url" % (flag)
output_file = "/root/daiwk_lp/lp_mining/lp_spider/all_%s_url.res" % (flag)

with open(input_file, 'r') as fin, \
         open(output_file, 'w') as fout:
    for line in fin:
        url = line.strip()
        hash_str = hashlib.md5()
        hash_str.update(url)
        out_str = '\t'.join([hash_str.hexdigest(), url])
        fout.write(out_str + '\n')

