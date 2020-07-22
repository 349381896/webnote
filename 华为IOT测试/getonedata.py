import requests,json


url = "https://49.4.92.191:8743/iocm/app/sec/v1.1.0/login"

payload = 'appId=BpF9vgFZl5prYtVY_H_jhGoaLpUa&secret=qxRYeyOfHaVPX7QWOIgKEQQBoK0a'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload,verify=False,cert=('E:/web学习/华为IOT测试/1_www.ycdemo.cn_bundle.crt','E:/web学习/华为IOT测试/2_www.ycdemo.cn.key'))
rdata = json.loads(response.text)
print(rdata)

print(rdata['accessToken'])
