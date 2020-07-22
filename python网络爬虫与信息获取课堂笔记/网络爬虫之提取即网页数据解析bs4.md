# 一、Beautiful Soup4库的使用
- BeautifulSoup库是解析、遍历、维护“标签树”的功能库
- Beautiful Soup库，也叫beautifulsoup或bs4库
    - 安装：pip install beautifulsoup4
    - 在程序中导入：from bs4 import BeautifulSoup
```
#创建BeautifulSoup对象
soup = BeautifulSoup("<p>data</p>","html.parser")
#·                    解析对象          解析器
```

## BeautifulSoup库的基本元素
```
<p>..</p>:标签Tag
例如：
<p                  class="title">...</p>
名称Name成对出现。  属性Attributes 0个或多个

```
**1)Beautiful Soup库解析器**
|       解析器          |   使用方法                        |           条件        |
|----------------------|-----------------------------------|-----------------------|
|   bs4的HTML解析器     |   BeautifulSoup(mk,"html.parser") |   安装bs4库           |
|   lxml的HTML解析器    |   BeautifulSoup(mk,"lxml")        |   pip install lxml    |
|   lxml的HTML解析器    |   BeautifulSoup(mk,"xml")         |   pip install lxml    |    
|   html5lib解析器      |   BeautifulSoup(mk,"html5lib")    |   pip install html5lib |        

**2)Beautiful Soup类的基本元素**
|       基本元素        |               说明                                            |
|-----------------------|--------------------------------------------------------------|
|   Tag                 |   标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾         |
|   Name                |   标签的名字，< p >..< /p >的名字'p'，格式：< tag >.name        |
|   Attributes          |   标签的属性，字典形式组织，格式：< tag >.attrs                 |
|   NavigableString     |   标签内非属性字符串，<>..</>中字符串，格式：< tag >.string      |
|   Comment             |   标签内字符串的注释部分，一种特殊的Comment类型                  |

**实例1**
```
import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

print(soup.title) #标题标签
print(soup.a) #返回第一个链接标签
print(soup.a.name) #返回a标签的名字
print(soup.a.parent.name) #返回父标签的名字


tag = soup.a
print(tag.attrs) #获得a标签的所有属性,字典形式
print(tag.attrs['class'])#获得a标签的class属性内容
print(tag.string)#返回标签包含的非属性字符串，可以跨多个标签层次
print(tag.comment)

```
## 2、基于bs4库的HTML内容遍历方法

**3)标签数的下行遍历**
|   属性        |               说明                                           
|---------------|--------------------------------------------------------------|
|   .contents   |   子节点的列表，将< tag>所有儿子节点存入列表                 
|   .childern   |   子节点的迭代类型，与.contents类似，用于循环遍历儿子节点 
|   .descendants|   子孙节点的迭代类型，包含所有子孙节点，用于循环遍历    

**实例2**                 
```
import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

print(soup.head) #获取head标签的内容
print(soup.head.contents) #获取head标签的儿子节点列表

print(soup.body.contents)#\n也是子节点
```

**4)标签数的上行遍历**
|   属性        |                           说明                                        
|---------------|-----------------------------------------------------------------------|
|   .parent     |   节点的父亲标签
|   .parents    |   节点先辈标签的迭代类型，用于循环遍历先辈节点

**实例3**
```
import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

print(soup.title.parent) #获取title标签的父标签
print(soup.html.parent)#获取html标签的父标签
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

```

**5)标签树的平行遍历**
- 平行遍历发生在同一个父节点下的各节点间

|       属性                    |                     说明                    
|-------------------------------|-----------------------------------------------------------------|
|   .next_sibling               |   返回按照HTML文本顺序的下一个平行节点标签
|   .previous_sibling           |   返回按照HTML文本顺序的上一个平行节点标签
|   .next_siblings              |   迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
|   .previous_siblings          |   迭代类型，返回按照HTML文本顺序的前续所有平行节点标签

**实例4**
```
import requests
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")


print(soup.a.next_sibling) #a标签的下一个平行节点
print(soup.a.next_sibling.next_sibling) #a标签的下一个平行节点的下一个平行节点
print(soup.a.previous_sibling)#a标签的上一个平行节点
print(soup.a.previous_sibling.previous_sibling)#a标签的上一个平行节点上一个平行节点

```

## 3、基于bs4库的HTML格式化和编码
==在bs4中使用prettify()方法对html格式化==
**实例5**
```
import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())  #对整个html格式化，标签和文本内容后添加换行符
print(soup.a.prettify()) #对于a标签进行格式化
```
**实例6（信息查找）**
```
import requests,re
from bs4 import BeautifulSoup

r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get("href")) #获取链接
```

## 4、文档中搜索

### 4-1、过滤器
- Beautiful Soup定义了很多搜索方法,这里着重介绍2个: find() 和 find_all() 
- < tag>(..) 等价于 < tag>.find_all(..)
- soup(..)  等价于 soup.find_all(..)
- <>.find_all(name,attrs,recursive,string,**kwargs)
    - 返回一个列表类型，存储查找的结果
    - name:对标签名称的检索字符串
        - 查找所有的< b>标签
        ` soup.find_all('b') #[<b>The demo python introduces several python courses.</b>]`

        - 查找a标签和b标签
        ` soup.find_all(['a','b']) `

        - 查找所有标签
        ` soup.find_all(True) `

        - 使用re查找所有b开头的标签
        ` soup.find_all(re.compile('b')) `

    - attrs:对标签属性值的检索字符串，可标注属性检索
        - 返回带有course属性的p标签
        ` soup.find_all('p','course') `

        - 返回属性中id等于link1的标签
        ` soup.find_all('p','course') `

    - recursive:是否对子孙全部检索，默认位True
    - string：<>..<>中字符串区域的检索字符串
        - 检索string内容为python的内容
        ` soup.find_all(string = re.compile("python")) `


**6)、find_all()扩展方法**
|       方法                    |                       说明                                        
|-------------------------------|-----------------------------------------------------------------------------------------|
|   <>.find()                   |   搜索且只返回一个结果，字符串类型，通.find_all()参数                     
|   <>.find_parents()           |   在先辈节点中搜索，返回列表类型，同.find_all()参数   
|   <>.find_parent()            |   在先辈节点中返回一个结果，字符串类型，同.find()参数
|   <>.find_next_siblings()     |   在后续平行节点中搜索，返回列表类型，同.find_all()参数
|   <>.find_next_sibling()      |   在后续平行节点中返回一个结果，返回字符串类型，同.find()参数
|   <>.find_previous_siblings() |   在前序平行节点中搜索，返回列表类型，同.find_all()参数
|   <>.find_previous_sibling()  |   在前序平行节点中返回一个结果，返回字符串类型，同.find()参数






