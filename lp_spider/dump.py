#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: dump.py
Author: root(root@baidu.com)
Date: 2016/07/24 23:14:52
"""
import pickle

import h5py
import numpy as np

crawled = "crawled.all"
dict_urlsign_lp = dict()
with open(crawled, 'r') as fin:
    for line in fin:
        url_sign = line.strip()
        output_path = '/root/daiwk_lp/lp_mining/output/'
        file_name = output_path + url_sign
        lp_info = b""
        with open(file_name, 'r') as file_url:
            for in_line in file_url:
                lp_info += in_line.strip()
        dict_urlsign_lp[url_sign] = lp_info

mode = "pickle"        
dump_file = "urlsign_lp.dump.pickle"
with open(dump_file, 'wb') as fout_dump:            
    pickle.dump(dict_urlsign_lp, fout_dump, -1) # latest binary protocol

with open(dump_file, 'rb') as fin_dump:
    data = pickle.load(fin_dump)

mode = "h5py"
dump_file = h5py.File("urlsign_lp.dump.hdf5", "w")
for k,v in dict_urlsign_lp.items():
    value = np.string_(v)
    dump_file.create_dataset(k, data=value)
dump_file.close()

dump_file = h5py.File("urlsign_lp.dump.hdf5", "r")
#urlsign_lp = dump_file["urlsign_lp"]
dump_file.close()


