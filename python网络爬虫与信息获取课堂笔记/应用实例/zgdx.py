from bs4 import BeautifulSoup
import requests
import bs4

kv = {"user-agent":"Mozilla/5.0"}

def  gethtml(url):
    try:
        r = requests.get(url,headers = kv, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag): #检测tr是否是标签类型，排除字符串等无关
            tds = tr.find_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string]) #批量加入

def printUnivList(ulist,num):
    print("{:^10}\t{:^15}\t{:^10}".format("排名","学校","地区")) #表头
    for i in range(num):
            u = ulist[i]
            print("{:^10}\t{:<15}\t{:^10}".format(u[0],u[1],u[2])) #表头


def main():
    uinfo=[]
    html = gethtml("http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html")
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #输出前20名大学
  

if __name__ == "__main__":
    main()