import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests


r = requests.get("http://www.xiachufang.com")  #获取网站首页
soup = BeautifulSoup(r.text)
print(soup.select('img'))


img_list = []


for img in soup.select('img'):
     if img.has_attr('data-src'): #判断是否有data-src属性
          img_list.append(img.attrs['data-src'])
     else:

          img_list.append(img.attrs['src'])


#初始化下载目录
image_dir = os.path.join(os.curdir,'images') #当前目录
# if not os.path.isdir(image_dir):           #判断是否存在此文件夹
#      os.mkdir(image_dir)       

for img in img_list:
    o = urlparse(img) 
    filename = o.path[1:].split('@')[0]
    filepath = os.path.join(image_dir,filename)
    if not os.path.isdir(os.path.dirname(filepath)):
         os.mkdir(os.path.dirname(filepath))
    url = '%s://%s/%s'%(o.scheme,o.netloc,filename)
    print(url)
    r =  requests.get(url)  #得到二进制数据 
    with open(filepath,'wb') as f:
         for chunk in r.iter_content(1024): #每次写1024字节
              f.write(chunk)
