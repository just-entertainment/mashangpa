import json
import time

import requests

import execjs
file=open('9.js', 'r', encoding='UTF-8').read()
ctx=execjs.compile(file)
#

sum=0
for i in range(1,21):
    data = ctx.call('getdata')
    m=data['m']
    tt=data['tt']
    print(m,tt)


    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-length": "85",
        "content-type": "application/json",
        "cookie": "sessionid=s49ju6qn2t50h9l2307ft6izk8v9wtmr; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1758990809,1759033220,1759252436,1759293978; HMACCOUNT=C94C6DE962162E86; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1759310274",
        "origin": "https://www.mashangpa.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.mashangpa.com/problem-detail/9/",
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    payload = {
        'm':m,
        'page':i,
        'tt':str(tt),
    }

    url = f'https://www.mashangpa.com/api/problem-detail/9/data/'
    res=requests.post(url=url,headers=headers,json=payload)##看看是json=，还是data=

    print(res.text)


    mes=res.json()

    print(mes['current_array'])
    for b in mes['current_array']:
        sum=sum+b
print(sum)