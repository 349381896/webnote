import socket   #Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
import datetime 


#创建服务端的socket对象socketserver
socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.119'
port = 8000
#绑定地址（包括ip地址会端口号）
socketserver.bind((host, port))
#设置监听  
socketserver.listen(5)
# #等待客户端的连接
# #注意：accept()函数会返回一个元组
# #元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)
clientsocket,addr = socketserver.accept()
 

plt.ion() #开启interactive mode 成功的关键函数  实现动态图的必须函数 开启交互（interactive）模式
plt.figure(1,figsize=(8,5),dpi=80)


x = [0]     #x轴序列
x_now = 0
y = [0]   #y轴序列

z = [0]
i =0 
 
#while循环是为了能让对话一直进行，直到客户端输入q
while True:
  
    #接收客户端的请求
    recvmsg = clientsocket.recv(1024)
    #把接收到的数据进行解码
    strData = recvmsg.decode("utf-8")
    
    #判断客户端是否发送q，是就退出此次对话
    if strData=='q':
        break
    
    data=strData.split(',')
    # print(data)
    print("温度------"+data[0]+" | "+"湿度------"+data[1])
    msg = "OK"
    #对要发送的数据进行编码
    clientsocket.send(msg.encode("utf-8"))
    
    i = i+1
    plt.clf() #清空画布上的所有内容
    x_now = i*0.1
    x.append(x_now)#模拟数据增量流入，保存历史数据
    y.append(float(data[0]))#模拟数据增量流入，保存历史数据
    z.append(float(data[1]))
    plt.xlabel('x')
    plt.ylabel(' temperature /C ; Humidity /%RH ')

    plt.plot(x,y,color="red",label="Temperature",linestyle="--")
    plt.plot(x,z, color="blue",label="Humidity",linestyle="-")
    plt.legend()
    plt.grid()  # 生成网格
    plt.pause(0.01)
    

    
socketserver.close()