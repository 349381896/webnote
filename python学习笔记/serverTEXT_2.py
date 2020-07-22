#coding:utf-8


import socket 

from  multiprocessing import Process

#API_ROOT_FILETEXT = ""

def handle_client(client_socket):
    #接受数据
    #request_data = recv()
    #print (request_data)
    #解析HTTP报文数据 request_data
    #提取请求方式
    #提取请求路径path
   #$ path = /index.html
    """处理客户端请求"""
    # 获取客户端数据
    request_data = client_socket.recv(1024)
    print("request_data:",request_data)

    #构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: my server\r\n"
    response_body = "hello word!"
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
    server_socket.bind(("192.144.215.88",443))       
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