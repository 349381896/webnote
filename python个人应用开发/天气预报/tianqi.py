#tianqi.py
from bs4 import BeautifulSoup
import requests
import re
url = "http://www.tianqihoubao.com/weather/top/ganzhou.html"
headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
 }
def getHTMLText(url):
    try:
        r = requests.get(url,headers = headers,timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

def main():
    datalist = []
    text = getHTMLText(url)
    soup = BeautifulSoup(text,"html.parser")
    trs = soup.find_all('tr')
    sting = ''
    for tr in trs[2:]:
        listtd = tr.find_all(['td','a'])
        del listtd[1]
        listtd =[str(x.string).strip() for x in listtd]  #处理数据，使其美观简洁显示
        datalist.append(listtd)
    return datalist
   

if __name__ == "__main__":
    main()