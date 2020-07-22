

# 一、requests库的使用

**1)、reques库的7个主要方法**
|           方法            |               说明                                             
|---------------------------|----------------------------------------------------------------|
|   requests.request()      |   构造一个请求，支撑以下各方法的基础方法，其余方法都只是再次封装request方法                         
|   requests.get()          |   获取HTML网页的主要方法，对应HTTP的GET                         
|   requests.head()         |   获取HTML网页头信息，对应于HTTP的HEAD
|   requests.post()         |   向HTML网页提交POST请求的方法，对应HTTP的POST
|   requests.put()          |   向HTML网页提交PUT请求方法，对应于HTTP的PUT
|   requests.patch()        |   向HTML网页提交局部修改请求，对应于HTTP的PATCH
|   requests.delete()       |   向HTML页面提交删除请求，对应于HTTP的DELETE

==r= requests.request(method,url,**kwargs)==
- method:请求方法，对应get/put/post等7种
- url:拟获取页面的url链接
- **kwargs:13个控制访问参数 
    - params:字典或字节序列，作为参数添加到url中
    - data:字典、字节序列或文件对象，作为Request的内容
    - json:JSON格式的数据，作为Request的内容
    - headers:字典，HTTP定制头
    - cookies:字典或CookieJar,Request中的cookie
    - auth:元组，支持HTTP认证功能
    - files:字典类型，传输文件
    - timeout:设定超时实践，秒为单位
    - proxies:字典类型，设定访问代理服务器，可以增加登入认证
    - allow_redirects:True/False,默认为True，重定向开关
    - stream:True/False,默认为True，获取内容立即下载
    - verify:True/False,默认为True,认证SSL证书开关
    - cert:本地SSL证书路径

==r = requests.get(url,params = None,**kwargs)==
- url:拟获取页面的url连接
- params:url中的额外参数，字典或字节流格式，可选
- **kwargs:12个控制访问参数，继承自request

==r = requests.post(url,data=None,json=None,**kwargs)==
- url:拟获取页面的url连接
- data:字典、字节序列或文件对象，作为Request的内容
- json:JSON格式的数据，作为Request的内容
-  **kwargs:12个控制访问参数，继承自request



**2)、Response对象属性**
|       属性                |               说明                                               
|---------------------------|-----------------------------------------------------------------|
|   r.status_code           |   HTTP请求的返回状态，200表示连接成功，404表示失败
|   r.txt                   |   HTTP响应内容的字符串形式，即url对应的页面内容
|   r.encoding              |   从HTTP header中猜测的响应内容编码方式
|   r.apparent_encoding     |   从内容中分析出的响应内容编码方法（备选编码方式）
|   r.conent                |   HTTP响应内容的二进制形式
|   r.headers               |   http响应内容的头部内容


**应用实列1**
```
import requests
r = requests.get("https://www.baidu.com/")
r.encoding = r.apparent_encoding
print(r.text)

```

**3)、HTTP请求方法**
- HTTP协议是一个基于“请求与响应”模式的、无状态、应用层协议
- HTTP协议采用URL作为定位网络资源的标识

|           方法            |                   说明                                           
|---------------------------|------------------------------------------------------------------|
|		POST                | 	向指定的资源提交要被处理的数据
|		GET                 | 	从指定的资源请求数据
|		HEAD                | 	与GET相同，但只返回HTTP报头，不返回文档主体
|		PUT                 | 	上传指定的URL表示
|		DELETE              |	删除指定资源
|		OPTIONS             |	返回服务器的HTTP方法
|		CONNECT             |	把请求连接转换到透明的TCP/IP通道
|       PATCH               |   请求局部更新URL位置的资源，即改变该处资源的部分内容

**4）、理解Requests库的异常**
|           异常                    |                       说明                                        
|-----------------------------------|-------------------------------------------------------------------|
|       requests.ConnectionError    |   网络连接错误异常，比如DNS查询失败、拒绝连接等      
|       requests.HTTPError:         |   HTTP错误异常
|       requests.URLRequired        |   URL缺失异常   
|       requests.TooManyRedirects   |   超过最大重定向次数，产生重定向异常                       
|       requests.ConnectionTimeout  |   连接远程服务超时
|       requests.Timeout            |   请求URL超时，产生超时异常

**5）、理解requests库的异常**
|       异常                |               说明                                               
|---------------------------|-----------------------------------------------------------------|
|   r.raise_for_status()      |   如果不是200，产生异常requests.HTTPError

**爬取网页的通用代码框架示例**
```
#爬取网页的通用代码框架示例
import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.baidu.com/"
    print(getHTMLText(url))

```

