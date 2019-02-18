#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

#page = requests.get("http://beijing.chineseoffice.com.cn/Template/office_complete.html")
for i in range(10):
    base_link = "http://beijing.chineseoffice.com.cn/Building/GetbuildingList?page=" + str(i)
    page = requests.get("http://beijing.chineseoffice.com.cn/Building/GetbuildingList")
    detail_page_link = "http://beijing.chineseoffice.com.cn/Template/office_details.html"
    page_dic = str(page.content.decode())
    #print(page.json())
    for build in page.json():
        print(build['id'], build['officeName'])
        build_link = detail_page_link + "?id=" + build['id']
        print(build_link)



# print(page.status_code)
# builds_doc = str(page.content,'utf-8')
# #print(page_doc)
# soup = BeautifulSoup(page_doc,"html.parser")
# print(soup)
# builds = soup.find_all(attrs={'class':'lone'})
# for build in builds:
#     print(build)