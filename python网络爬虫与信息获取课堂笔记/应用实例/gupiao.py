import requests
from bs4 import BeautifulSoup
import traceback
import re

kv = {"user-agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
cookies = {"thw=cn":"t=254ecf83ad9b49c70d383c71e214fab2;cna=kbBgFFO2dU8CAXFzKR/6/wq5; tg=0;enc=xWaBwIc%2BqZfhPca6P6g4cz34emAsVK3LjzRsT%2FkMfk5Ja31%2BmjMxGvBDJ%2B82Q2pJLJ83dUH5lBPAw%2BpI53L4%2BQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156"}
def  gethtml(url):
    try:
        r = requests.get(url,headers = kv, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return r.text
    except:
        return "爬取失败"
    
def getStockList(lst,stockURL):
    html = gethtml(stockURL)
    soup = BeautifulSoup(html,"html.parser") 
    print(soup.findAll('tr'))

def getStockInfo(lst,stockURL,fpath):
    pass

def main():
    stock_lsit_url = "http://quote.eastmoney.com/stocklist.html" 
    stock_info_url = "'https://gupiao.baidu.com/stock/"
    output_file = "E:\web学习\python网络爬虫与信息获取课堂笔记\static\images/gu[iaoInfo.txt"
    slist = []  
    getStockList(slist,stock_lsit_url)  #获取股票列表
    getStockInfo(slist,stock_info_url,output_file) #获取指定股票信息，并保存至文件



if __name__ == "__main__":
    main()