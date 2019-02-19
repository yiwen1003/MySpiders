#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getBuildsInfo():
    url = "http://beijing.chineseoffice.com.cn/Building/GetbuildingList"
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':'application/json, text/javascript, */*; q=0.01'
    }
    for i in range(10):
        data = "page=%s" % str(i)
        listPage = requests.post(url,data=data)
        page = requests.get("http://beijing.chineseoffice.com.cn/Building/GetbuildingList")
        detail_page_link = "http://beijing.chineseoffice.com.cn/Template/office_details.html"
        page_dic = str(listPage.content.decode())
        #print(page.json())
        for build in listPage.json():
            print(build['id'], build['officeName'])
            build_link = detail_page_link + "?id=" + build['id']
            print(build_link)

def saveToFile():
    pass


def saveToXML():
    pass
