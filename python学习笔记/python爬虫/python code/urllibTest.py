
#-*- coding:utf-8 -*-
import json
import urllib
from urllib import request as urlreq


#接收一个字符串对象
r = urlreq.urlopen('http://httpbin.org/get')
print(dir(r))

text = r.read() #读取response的内容

print(r.status , r.reason) #http返回状态码和msg

r.close()
obj = json.loads(text)#返回内容是json格式，load函数加载
print(obj)

#r.headers是一个HTTPMessage对象
print(r.headers)


#添加自定义的头信息
req = urlreq.Request("http://httpbin.org/user-agent")
req.add_header("User-Agent","curl 7.01")
#接收一个urllib.request.Request对象，作为参数
r = urlreq.urlopen(req)
resp = json.load(r)

print("User-agent: ",resp["user-agent"])


#带用户名的登入
auth_handler = urlreq.HTTPBasicAuthHandler()
auth_handler.add_password(realm="httpbin auth",uri="http://httpbin.org/basic-auth/xiao/qwertyuiop",
                            user='xiao',passwd="qwertyuiop")

opener =urlreq.build_opener((auth_handler))
urlreq.install_opener(opener)

r = urlreq.urlopen('http://httpbin.org')

print(r.read().decode('utf-8'))

#使用GET参数
params = urllib.parse.urlencode({'name':'xiao','years':2019})
url = 'http://httpbin.org/get?%s' % params
with urlreq.urlopen(url) as f:
    print(json.load(f)['args'])
    
#使用POST方法传递参数
data = urllib.parse.urlencode({'name':'ming','ages':22}) #编码
data = data.encode()
with    urlreq.urlopen('http://httpbin.org/post',data)  as  f:
    print(json.load(f))
    
#使用代理IP请求远程url
# proxy_handler = urlreq.ProxyHandler({'http':'202.183.84.43:8888'})  #添加代理

# #proxy_auth_handler =  urlreq.ProxyBasicAuthHandler({"http':'http://iguye.com:41801}") #带用户登入的代理接口

# opener = urlreq.build_opener(proxy_handler)

# r=opener.open('http://httpbin.org/ip')

# print(r.read())

#urlparse模块    将字符串拆分为可用的http链接
o=urllib.parse.urlparse("http://httpbin.org/get")

print(dir(o)) 
print(o.hostname)