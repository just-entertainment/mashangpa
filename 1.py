import requests


headers= {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cookie": "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0=1758604327; HMACCOUNT=C94C6DE962162E86; sessionid=s49ju6qn2t50h9l2307ft6izk8v9wtmr; Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0=1758605894",
    "priority": "u=1, i",
    "referer": "https://www.mashangpa.com/problem-detail/2/",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}

allsum=0
sum=0
for i in range(1,21):

    url = f'https://www.mashangpa.com/api/problem-detail/1/data/?page={i}'
    res=requests.get(url=url,headers=headers)
    res=res.json()
    # print(res['current_array'])
    for a in res['current_array']:
        sum=sum+a

print('sum:',sum)