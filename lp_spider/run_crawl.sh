#!/bin/bash

flag=$1
python=/usr/bin/python

function prepare()
{
    flag=$1
    echo "start $flag $FUNCNAME AT " `date`
    $python gen_md5.py $flag
    echo "end $flag $FUNCNAME AT " `date`
    return 0
}

function crawl()
{
    flag=$1
    echo "start $flag $FUNCNAME AT " `date`
    mkdir -p ../output/$flag/
    /bin/rm -rf ../output/$flag/*
    #export http_proxy='http://agent.baidu.com:8118'
    #export https_proxy='http://agent.baidu.com:8118'
    scrapy crawl $flag
    ls -l ../output/$flag/ | grep -v /| grep -v total| awk -F' ' '{print $NF}' | sort | uniq > crawled.all.$flag
    awk -F' ' '{print $1}' ./all_${flag}_url.res | sort | uniq > to_crawl.all.$flag
    echo "end $flag $FUNCNAME AT " `date`
    return 0
}

function dump()
{
    flag=$1
    echo "start $flag $FUNCNAME AT " `date`
    $python dump.py $flag
    echo "end $flag $FUNCNAME AT " `date`
    return 0
}

function main()
{
    prepare $flag
    crawl $flag
    dump $flag
}
main 2>&1
