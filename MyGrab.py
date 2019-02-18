#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree


def tieba_grab(page):
    data = {"ie": "utf-8", "kw": "python爬虫吧", "pn": page}
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"}
    url = "https://tieba.baidu.com/f?kw=%E7%88%AC%E8%99%AB&ie=utf-8&pn="+str(page)
    # url1 = "https://tieba.baidu.com/f"
    page = requests.get(url)
    print(page.url)
    root = etree.HTML(page.text)
    results = root.xpath("//ul[@class='threadlist_bright j_threadlist_bright']/li[@class=' j_thread_list clearfix']") #do not include top-list不包含置顶部分
    length = len(results)
    print(length)
    for i in range(length):
        title = results[i].xpath(".//div[@class='threadlist_title pull_left j_th_tit ']/a/text()")
        for i in title:
            print(i)


if __name__ == '__main__':
    for i in range(10):
        tieba_grab(i*50)
