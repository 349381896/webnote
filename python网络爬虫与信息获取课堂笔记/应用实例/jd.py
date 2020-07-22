import requests

url = "https://item.jd.com/14157116051.html"
kv = {"user-agent":"Mozilla/5.0"}
def getHTMLText(url):
    try:
        r = requests.get(url,headers = kv,timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

def main():
    
    print(getHTMLText(url))

if __name__ == "__main__":
    main()