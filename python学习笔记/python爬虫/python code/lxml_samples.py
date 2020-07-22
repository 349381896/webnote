from lxml import etree
import  requests
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

selector = etree.HTML(html_doc)

#取出页面内所有的链接
links = selector.xpath('//p[@class="story"]/a/@href')
for link in links:
    print(link)
    
r  = requests.get('http://iguye.com/books.xml')
se = etree.HTML(r.text)
print(se.xpath('book'))

#选取书店下所有的书本的作者名字
print(se.xpath('//bookstore/book/author/test()'))

#选取书店下所有的书本的语言
print(se.xpath('//bookstore/book/title/@lang'))

#选取书店下第一本书的标题
print(se.xpath('//bookstore/book[1]/title/text()'))


#选取书店下最后一本书的标题
print(se.xpath('//bookstore/book[last()]/title/text()'))

#选取书店下倒数第二本书的标题
print(se.xpath('//bookstore/book[last()-1]/title/text()'))

#选取书店下前两本书的标题
print(se.xpath('//bookstore/book[position()<3]/title/text()'))

#选取所有分类为web的书本
print(se.xpath('//book[@cetegory="web"]/title/text()'))

#选取所有价格大于30.00的书本
print(se.xpath('//book[price>30.00]/price/text()'))

#选取所有class属性中包含book的书本的class属性
print(se.xpath('//book[contains(@class,"book")]/@class'))

print(se.xpath('//head'))