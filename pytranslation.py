#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_= luo
import urllib.request
import urllib.parse
import json
import time

while 1:
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

    data = {}
    string1 = input('请输入想要翻译的内容(输入q退出):')
    if string1 == 'q':
        break
    data['i'] = string1[:]
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = ' 15499363267329'
    data['sign'] = ' 540a5f3af3b1e2d038323ab8fc4a771e'
    data['ts'] = ' 1549936326732'
    data['bv'] = '65db4e7e1a2a0ee160ea1e66436196cd'
    data['doctype'] = 'json'
    data['version'] = ' 2.1'
    data['keyfrom'] = ' fanyi.web'
    data['action'] = ' FY_BY_CLICKBUTTION'
    data['typoResult'] = ' false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
    time.sleep(3)
