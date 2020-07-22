#提交搜索关键词
import requests

url = "http://suggestion.baidu.com/su"
kv = {"user-agent":"Mozilla/5.0"}
param = {"wd":"python"}
def getHTMLText(url):
    try:
        r = requests.get(url,params=param,headers = kv,timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        # print(r.request.url)
        return r.text
    except:
        return "产生异常"

def main():
    
    print(getHTMLText(url))

if __name__ == "__main__":
    main()




