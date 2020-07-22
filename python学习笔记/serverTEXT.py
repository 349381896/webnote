#coding:utf-8


import socket 
import re
from  multiprocessing import Process

#设置静态文件根目录
API_ROOT_FILETEXT = ""

def handle_client(client_socket):
    
    #接受数据
    #request_data = recv()
    #print (request_data)
    #解析HTTP报文数据 request_data
    #提取请求方式
    #提取请求路径path
    
    """处理客户端请求"""
    # 获取客户端数据
    request_data = client_socket.recv(1024)
    print("request_data:",request_data)
    request_lines=request_data.splitlines()  #splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表
    
    #解析请求报文
    request_start_line = request_lines[0] #GET / HTTP/1.1
    #提取用户请求文件名
    file_name = re.match(r"\w+ (/[^ ]*)",request_start_line).group(1)#正则表达式
    #\w  匹配任何字母与数字字符；这相当于类 [a-zA-Z0-9_]。      
    #[^5] 将匹配除 '5' 之外的任何字符
    try:
        #打开文件
        file = open(API_ROOT_FILETEXT+file_name, "rb") #只读2进制
    except IOError:
        response_start_line = "HTTP/1.1 400 Not Found\r\n"
        response_headers = "Server: my server\r\n"
        response_body = "the file not find"
    else:
        file_data = file.read()
        file.close()

   
    #构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: my server\r\n"
    response_body = file_data
    response = response_start_line + response_headers + "\r\n" + response_body 
    print("response data:", response)

    #向客户端发送数据
    client_socket.send(bytes(response,"utf-8"))
    #                       转换的对象   对象的编码格式
    client_socket.close()


#tcp socket 服务端
 
if __name__ =="_main_":
                           #   常量           选择TCP 
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(("192.144.215.88",8000))       
    server_socket.listen(128) #监听队列大小为128


    while True:
    #                   元组类型    
        client_socket,client_adderess = server_socket.accept()
    # 接受返回的socket    ip地址
        print("[%s,%s]用户已连接"  %client_adderess)
        handle_client_process = Process(target=handle_client,args=(client_socket,))  #进程
    #                回调函数             接受参数
        handle_client_process.start()
        client_socket.close()