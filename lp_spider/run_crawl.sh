#!/bin/bash

flag=$1
python=/usr/bin/python
data_path=/notebooks/lp_output/

function prepare()
{
    flag=$1
    echo "start $flag $FUNCNAME AT " `date`
    $python gen_md5.py $flag $data_path
    echo "end $flag $FUNCNAME AT " `date`
    return 0
}

function crawl()
{
    flag=$1
    echo "start $flag $FUNCNAME AT " `date`
    mkdir -p $data_path/$flag/
    /bin/rm -rf $data_path/$flag/*
    #export http_proxy='http://agent.baidu.com:8118'
    #export https_proxy='http://agent.baidu.com:8118'
    scrapy crawl $flag
    ls -l $data_path/$flag/ | grep -v /| grep -v total| awk -F' ' '{print $NF}' | sort | uniq > $data_path/crawled.all.$flag
    awk -F' ' '{print $1}' $data_path/all_${flag}_url.res | sort | uniq > $data_path/to_crawl.all.$flag
    echo "end $flag $FUNCNAME AT " `date`
    return 0
}

function dump()
{
    flag=$1
    echo "start $flag $FUNCNAME AT " `date`
    $python dump.py $flag $data_path
    echo "end $flag $FUNCNAME AT " `date`
    return 0
}

function main()
{
    prepare $flag
#    crawl $flag
#    dump $flag
}
main 2>&1
