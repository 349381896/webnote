html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#创建一个BeautifulSoup对象
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(dir(soup))
print(soup.prettify())
print(soup.title.text) 

#判断soup.a的可用方法
print('判断soup.a的可用方法:',dir(soup.a))

#取出第一个a标签的所有属性
print("取出第一个a标签的所有属性:",soup.a.attrs)

#取出a标签的href属性
print("取出a标签的href属性:",soup.a.attrs['href'])

#判断是否有class属性
print('判断是否有class属性:',soup.a.has_attr('class'))

#取出第一个p标签下所有的子节点  取出来是一个迭代器，用list整合一下
print(type(soup.p.children))
print(list(soup.p.children)[0].text)

#取出页所有的链接
print("取出页所有的链接:")
for link in soup.find_all('a'):
    print(link.get('href'))
  
#支持css选择器  选择器语法
print(soup.select('#link1'))#查找id='link1'的标签       #+ID
print(soup.select('p.story'))#查找类为story的p标签        .+类名

#使用lxml解析，c库，解析速度快
soup_lxml = BeautifulSoup(html_doc,'lxml')
print('lxml使用：',soup_lxml.a)