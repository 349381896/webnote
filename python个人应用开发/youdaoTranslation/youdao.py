#youdao.py
import requests
from bs4 import BeautifulSoup
import traceback
import re
import json
import time,random

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        # "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1076696971@10.168.8.63;JSESSIONID=aaaZ6s5m9DVmYf8g3QoDw;OUTFOX_SEARCH_USER_ID_NCOO=473292646.5080033;___rl__test__cookies=1543228484656",
        "Host": "fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.100Safari/537.36OPR/56.0.3051.104X-Requested-With:XMLHttpRequest"
    }

data = {};
data['i']                      =        "政府"
data['from']                   =        'AUTO'
data['to']                     =        'AUTO'
data['smartresult']            =        'dict'
data['client']                 =        'fanyideskweb'
data['salt']                   =        '15927035175814'
data['sign']                   =        '52f9befe3ae6d254d3155659275a4bfd'
data['ts']                     =        '1592703517581'
data['bv']                     =        'd17d9dd026a611df0315b4863363408c'
data['doctype']                =        'json'
data['version']                =        '2.1'
data['keyfrom']                =        'fanyi.web'
data['action']                 =        'FY_BY_REALTlME'


def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)

    soup = BeautifulSoup(web_data.text, 'html.parser')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    # print(proxy_list)
    proxy_ip = random.choice(proxy_list) #随机获取
    prox = {'http': proxy_ip}
    return prox


def get_salt():
    import time, random
    salt = int(time.time() * 1000) + random.randint(0, 10)
    return salt

def get_md5(v):
    import hashlib
    md5 = hashlib.md5()  # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
    md5.update(v.encode('utf-8'))  # 要对哪个字符串进行加密，就放这里
    value = md5.hexdigest()  # 拿到加密字符串
    return value

def get_sign(key, salt):
    sign = 'fanyideskweb' + key + str(salt) + 'n%A-rKaT5fb[Gy?;N5@Tj'
    sign = get_md5(sign)
    return sign

def get_ts():
    # 根据当前时间戳获取ts参数
    s = int(time.time() * 1000)
    return str(s)


def getHTMLText(url,data,headers,proxies):
    try:
        r = requests.post(url,headers = headers,data = data,proxies=proxies)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        
        return r.text
    except:
        return "产生异常"

def main(input,changes="AUTO>>AUTO"):
    salt = get_salt()
    fromto=re.split(r'>>',changes)
    data['from']                   =        fromto[0]
    data['to']                     =        fromto[1]
    # print(fromto)
    data['i'] = input
    data['salt']                   =        str(salt)
    data['sign']                   =        str(get_sign(input,salt))
    data['ts']                     =        str(get_ts())
    r=getHTMLText(url,data,headers,proxies={'http':'http://ycdemo.cn:41801'})
    print(r)
    t = json.loads(r)#将已编码的json字符串为python对象
    Type = t['type']
    translateResult = t['translateResult']
    src = translateResult[0][0]['src']
    tgt = translateResult[0][0]['tgt'] #基本常用翻译结果
    try:
        entries = ''
        for index in t['smartResult']['entries'][1:]: #详细翻译结果
            entries = entries + index.strip('\r\n') +' '    
        print(entries)
        return [tgt,entries]
    except:
        return [tgt,'']
    


if __name__ == "__main__":
    main('反馈','zh-CHS>>en')