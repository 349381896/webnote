# 一、scrapy爬虫框架

## 1、scrapy的基本介绍
- scrapy的安装：pip install scrapy
    - 测试：scrapy -h
- Scrapy不是一个函数功能库，而是一个爬虫框架
    - 爬虫框架是实现爬虫功能的一个软件结构和功能组件集合。
    - 爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫。

![scrapy爬虫框架1](https://img-blog.csdnimg.cn/20200314102145483.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTUxNTkz,size_16,color_FFFFFF,t_70)

![scrapy爬虫框架2](https://img-blog.csdnimg.cn/20200314102237650.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTUxNTkz,size_16,color_FFFFFF,t_70)

### 1-1 Scrapy框架组成部分(5个模块)
|       模块            |           说明                    
|-----------------------|------------------------------------------------------------|
|   Engine              |   控制价所有模块之间的数据流。根据条件触发事件
|   Downloarder         |   根据请求下载网页。不需要用户修改
|   Scheduler           |   对所有爬取请求进行调度。不需要用户修改
|   Spider              |   解析Downloader返回的响应（Response)。产生爬取页（scraped item)。产生额外的爬取请求（Request)。需要用户编写配置代码。
|   Item Pipelines      |   以流水线方式处理Spider产生的爬取页。由一组操作顺序组成，产生类似流水线，每个操作是一个Item Pipeline类型。可能操作包括：清理、校验和查重爬取项中的HTML数据、将数据存储到数据库。需要用户编写配置代码。

### 1-2 2个中间件
- Downloader Middleleware
    - 目的：实施Engine、Scheduler和Downloarder之间进行用户可配置的控制
    - 功能：修改、丢弃、新增请求或响应
    - 用户可以编写配置代码
- Spider Middleware
    - 目的：对请求和爬取项的再处理
    - 功能：修改、丢弃、新增请求或爬取项
    - 用户可以编写配置代码

## 2、request库和Scarpy爬虫的比较
**1）相同点**
- 两者都可以进行页面请求和爬取，python爬虫的两个重要技术路线
- 两者可用性好，文档丰富、入门简单
- 两者都没有处理js、提交表单、应对验证码等功能（可扩展）

**2）不同点requests VS Scrapy**
|   requests                |           Scrapy
|---------------------------|---------------------------------------------|
|   页面级爬虫              |   网站级爬虫
|   功能库                  |   框架
|   并发性考虑不足，性能较差 |   并发性好，性能较高
|   重点在于页面下载         |   重点在于爬取结构
|   定制灵活                |   一般定制灵活，深度定制困难
|   上手十分简单            |   入门稍难

## 3、Scrapy爬虫的常用命令
- scrapy是为持续运行设计的专业爬虫框架，提供操作的Scrapy命令行
    - scrapy命令行格式：
        - scrapy \<command>[options][args]

### 3-1 Scrapy常用命令
|       命令        |           说明                                        |           格式
|-------------------|-------------------------------------------------------|---------------------------------------------|
|   startproject    |   创建一个新工程                                      |   scrapy startproject \<name>[dir]       
|   genspider       |   创建一个爬虫                                        |   scrapy genspider [options]\<name>\<domain>
|   settings        |   获取爬虫配置信息                                    |   scrapy settings[options]
|   crawl           |   运行一个爬虫                                        |   scrapy crawl \<spider>  
|   list            |   列出工程中所有爬虫                                  |   scrapy list
|   shell           |   启动URL调试命令行                                   |   scrapy shell [url]                                       

### 3-2 scrapy产生步骤
-  步骤1：建立一个Scrapy爬虫工程:scrapy startproject python123demo（生成一个工程文件夹）
```
#工程的文件组合：
python23demo/                   ---------->         外层目录
    |____ scrapy.cfg            ---------->         部署scrapy爬虫的配置文件，一般服务器用
    |____ python123demo/        ---------->         scrapy框架的用户自定义python代码
        |____ __init_.py        ---------->         初始化脚本
        |____ items.py          ---------->         Items代码模板（继承类）
        |____ middlewares.py    ---------->         Middlewares代码模板（继承类）
        |____ pipelines.py      ---------->         Pipelines代码模板（继承类）
        |____ settings.py       ---------->         Scrapy爬虫的配置文件
        |____ spiders/          ---------->         Spiders代码模板目录（继承类）
            |____ __init__.py   ---------->         初始文件，无需修改
            |____ __pycache.py  ---------->         缓存目录，无需修改
```
- 步骤2：在工程中产生一个Scrapy爬虫(工程目录下：scrapy genspider demo python123.io) 
    - 在spiders目录下生成了demo.py文件
```
# -*- coding: utf-8 -*-
#demo.py
import scrapy


class DemoSpider(scrapy.Spider): #必须继承scarpy.Spider类
    name = 'demo' #爬虫名字
    allowed_domains = ['python123.io'] #最开始用户提交的域名，爬虫只爬取该域名下的链接
    start_urls = ['http://python123.io/'] #

    def parse(self, response):  #解析页面预定义函数
        pass

#parse()用于处理响应，解析响应内容形成字典，发现新的URL爬取请求
```

- 步骤3：配置产生的spider爬虫（修改demo.py文件）
```
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open (fname,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.'% name)
        pass
```

- 步骤4：运行爬虫，获取网页（工程目录下:scrapy crawl demo）

### 3-3 yield(生成器)关键字的使用
- 生成器是一个不断产生值的函数
- 包含yield语句的函数是一个生成器
- 生成器每次产生一个值（yield语句）,函数被冻结，被唤醒后再产生一个值。
**举例**
```
def gen(n):
    for i in range(n):
        yield i**2
for i in gen(5):
    print(i,"",end="")  

输出：0 1 4 9 16

```
**使用yield更改scrapy爬虫**
```
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    def start_requests(self):
        urls = [
                  'http://python123.io/ws/demo.html'  
               ]
        for url in urls:
            yield scrapy.Request(url=url,callable=self.parse)

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open (fname,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.'% name)

```

## 4、Scrapy爬虫的基本使用
### 4-1 Scrapy爬虫的使用步骤
- 步骤1：创建一个工程和Spider模板
- 步骤2：编写Item Pipeline
- 步骤3：编写Spider
- 步骤4：优化配置策略

### 4-2 Scrapy爬虫的数据类型
- Request类：class scrapy.http.Request()
    - Request对象表示一个HTTP请求
    - 由Spider生成，由Downloader执行

**Request类**

|       属性或方法              |                       说明
|-------------------------------|----------------------------------------------------------------------------|
|   .url                        |   Request对应的请求URL地址
|   .method                     |   对应的请求方法，'GET''POST'等
|   .headers                    |   字典类型风格对应的请求头
|   .body                       |   请求内容的主主体，字符串类型
|   .meta                       |   用户添加的扩展信息，在Scrapy内部模块间传递信息用
|   .copy()                     |   复制该请求

- Response类：class scrapy.http.REsponse()
    - Response对象表示一个HTTP响应
    - 由Downloader生成，由Spider处理
**Response类型**

|       属性或方法              |                       说明
|-------------------------------|----------------------------------------------------------------------------|
|   .url                        |   Response对应的请求URL地址
|   .status                     |   HTTP状态码，默认是200
|   .headers                    |   Response对应的头部信息
|   .body                       |   Response对应的内容信息，字符串类型
|   .flags                      |   一组标记
|   .request                    |   产生Response类型对应的Requset对象
|   .copy()                     |   复制该响应

- Item类：class scrapy.item.Item()
    - Item对象表示一个从HTTP页面中提取的信息内容
    - 由Spider生成，由Item Pipeline处理
    - Item类似字典类型，可以按照字典类型操作

### 4-3 scrapy爬虫提取信息的方法
- Scrapy爬虫支持多种HTML信息提取方法
    - Beautiful Soup
    - lxml
    - re
    - XPath Selector
    - CSS Selector

**CSS Selsector的基本使用**
> \<HTML>.css('a::attr(href)').extrac()
>     标签名称_|        |__标签属性
