from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.xiachufang.com")  #获取网站首页
soup = BeautifulSoup(r.text)
print(soup.select('img'))