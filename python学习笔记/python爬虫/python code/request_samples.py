#-*- coding:utf-8 -*-
import requests

print(dir(requests))

#发起get请求
r = requests.get('http://httpbin.org/get',params={'name':'xiao'})
print(r.status_code,r.reason)
print(r.text)
print(r.json())

#发起POST请求
r = requests.post('http://httpbin.org/post',data={'a':1,'b':2})
print(dir(r))
print(r.json())

#自定义headers请求
headers = {'User-Agent':'curl 7.01'}
r = requests.get('http://httpbin.org/headers',headers=headers)
print('自定义的headers的请求',r.json())


#带cookies的请求
cookies = dict(userid="12345",token = 'xxxxxxxxxx') #字典
r = requests.get('http://httpbin.org/cookies',cookies = cookies)
print("带cookies的请求：",r.json())

#Basic-auth认证请求
r = requests.get('http://httpbin.org/basic-auth/xiao/qwertyuiop',auth=('xiao','qwertyuiop'))
# print(r.text)
print('带Basic-auth认证的请求',r.json())

# #主动抛出状态码异常
# bad_r = requests.get('http://httpbin.org/status/402')
# bad_r.raise_for_status()    #


#使用request.Session对象请求
#创建一个Session对象
s = requests.Session()
#session对象会保存服务器返回的set-cookies头信息里面的内容
s.get('http://httpbin.org/cookies/set/userid/123456789')
s.get('http://httpbin.org/cookies/set/token/xxxxxxxxxxx')
#下一次请求会将本地所有的cookies信息自动添加到头信息里面
r = s.get("http://httpbin.org/cookies")
print("检查session中的cookies",r.json())

#在request中使用代理
print('不使用用代理：',requests.get('http://httpbin.org/ip').json())
print("使用代理：",requests.get('http://httpbin.org/ip',proxies={'http':'http://ycdemo.cn:41801'}).json())
                                                                #个人服务器代理
#超时请求
r=requests.get('http://httpbin.org/delay/4',timeout = 5)
print(r.text)