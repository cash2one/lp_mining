#!/usr/bin/env python
# -*- coding: gbk -*-
########################################################################
# 
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: gen_word2vec.py
Author: root(root@baidu.com)
Date: 2016/07/25 22:20:12
"""
import os
import re

import gensim
import jieba
import jieba.posseg
import jieba.analyse

##stop_words_file = ""
##user_dict_file = ""
##jieba.analyse.set_stop_words(stop_words_file)
##jieba.load_userdict(user_dict_file)

jieba.enable_parallel(20)
file_doc = '/notebooks/wise_title_desc_bigflow.all.0724.head'
sentences = []
with open(file_doc, 'rb') as fin:
    for line in fin:
        vals = line.strip()
        ##re.sub(u'([\u4E00-\u9FA5a-zA-Z0-9+_]+)', r'', vals.decode('gbk')) ## removed special symbols..
        sentence = list(jieba.cut(vals, cut_all=True, HMM=True))
        sentence2 = list(jieba.posseg.cut(vals))
        #for i in sentence2:
        #    print i.encode('gbk')
        sentences.append(sentence)

model = gensim.models.Word2Vec(sentences, min_count=1, workers=3, size=50)
output_path = '/notebooks/lp_output/lp_feature/'
utf8_model = output_path + "w2v.model.utf8"
gbk_model = output_path + "w2v.model.gbk"
model.save_word2vec_format(utf8_model, binary=False)
os.system('iconv -f utf8 -t gbk %s -o %s' % (utf8_model, gbk_model))
