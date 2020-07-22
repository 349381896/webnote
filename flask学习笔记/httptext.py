import requests

url = "http://127.0.0.1:5000/api/inituser"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\nycdemo\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\nqwertyuiop\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "8453755e-c3ec-450c-9278-1f22af9855d2,dcc4d9e5-4417-48cd-829a-1f74112bbd4e",
    'Host': "127.0.0.1:5000",
    'Content-Type': "multipart/form-data; boundary=--------------------------048564815704769849066389",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "292",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)