import json
import time

import requests

import execjs
file=open('7getdata.js', 'r', encoding='UTF-8').read()
ctx=execjs.compile(file)
#

sum=0
for i in range(1,21):
    a = ctx.call('get_data')
    m = str(a['m'])
    ts = str(a['ts'])
    x = str(a['x'])
    # print(m,ts,x)

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "cookie": "sessionid=s49ju6qn2t50h9l2307ft6izk8v9wtmr; Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1758604327,1758700815; HMACCOUNT=C94C6DE962162E86; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1758701499",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.mashangpa.com/problem-detail/6/",
        "M": m,
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "Ts": ts,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
    }
    params = {
        'page': i,
        'x':str(x),
    }

    url = f'https://www.mashangpa.com/api/problem-detail/7/data/'
    res=requests.get(url=url,headers=headers,params=params)
    # print(res.url)
    # print(res.json())
    data=res.json()['r']
    mes=ctx.call('xxxxoooo',data)
    mes=json.loads(mes)  ##注意转一下类型
    print(mes['current_array'])
    for b in mes['current_array']:
        sum=sum+b
print(sum)