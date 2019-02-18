#!/usr/bin/env python
# -*- coding:utf-8 -*-

import docx
import urllib.request
import urllib.parse
import json
import time
import random
import hashlib

def read_docx(fileName):
    doc = docx.Document(fileName)
    for paragraph in doc.paragraphs:
        print(paragraph.text)


def youdao():
    #url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {}

    content = 'world'
    salt = str(time.time()*1000 + random.randint(1, 10))
    u = 'fanyideskweb'
    c = 'ebSeFb%=XZ%T[KZ)c(sy!'
    sign = hashlib.md5((u + content + salt + c).encode('utf-8')).hexdigest()

    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = salt
    data['sign'] = sign
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'false' # 'true'



    data = urllib.parse.urlencode(data).encode('utf-8')
    #request = urllib.request.Request(url=url, data=data, method='POST')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print('翻译的结果：%s' % target)


if __name__ == '__main__':
    #read_docx(fileName = r'D:\Longmen.docx')
    youdao()


