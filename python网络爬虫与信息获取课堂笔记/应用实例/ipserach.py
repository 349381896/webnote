import requests
url = "http://m.ip138.com/ip.asp"
param = {"ip":"223.83.89.135"}
kv = {"user-agent":"Mozilla/5.0"}
def getHTMLText(url):
    try:
        r = requests.get(url,params= param,headers = kv ,timeout = 30)
        print(r.request.url)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        
        return r.text
    except:
        return "产生异常"
def main():
    print(getHTMLText(url))

if __name__ == "__main__":
    
    main()

