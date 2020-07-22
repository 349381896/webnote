# 1、https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306

# 2、https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44

# 3、https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88
import requests
import re

kv = {"user-agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
cookies = {"thw=cn":"t=254ecf83ad9b49c70d383c71e214fab2;cna=kbBgFFO2dU8CAXFzKR/6/wq5; tg=0;enc=xWaBwIc%2BqZfhPca6P6g4cz34emAsVK3LjzRsT%2FkMfk5Ja31%2BmjMxGvBDJ%2B82Q2pJLJ83dUH5lBPAw%2BpI53L4%2BQ%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156"}
def  gethtml(url):
    try:
        r = requests.get(url,headers = kv,cookies = cookies, timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return r.text
    except:
        return "爬取失败"
    
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            tiltle = eval(tlt[i].split(":")[1])
            ilt.append(([price,tiltle]))
    except:
        print("解析异常")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1])) 

def main():
    goods = "书包"
    depth = 2   #深度
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList= []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = gethtml(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)    


if __name__ == "__main__":
    main()