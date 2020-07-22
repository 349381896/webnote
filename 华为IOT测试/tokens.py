
import requests,json
url = "https://49.4.92.191:8743/iocm/app/cmd/v1.4.0/deviceCommands?appId=BpF9vgFZl5prYtVY_H_jhGoaLpUa"
payload = '''{
                    "deviceId": "3d15441f-9ee1-45a9-8d1c-b20a893160c3",
                    "command": {
                    "serviceId": "data",
                    "method": "command",
                    "paras": {
                    "on_off":1,
                    "value": 5
                    }
                    },
                   
                    "callbackUrl": "http://32603c828o.wicp.vip/api/test",
                    "maxRetransmit":1
                }'''
payload = json.loads(payload)
payload['deviceId'] = '3d15441f-9ee1-45a9-8d1c-b20a893160c3'
payload['command']['paras']['on_off'] = 0
payload['command']['paras']['value'] = 28
payload = json.dumps(payload)
token = '8068571ceb3367edb9938e3bbc163a1'
headers = {
    'Content-Type': 'application/json',
    'app_key': 'BpF9vgFZl5prYtVY_H_jhGoaLpUa',
    'Authorization': token
}
response = requests.request("POST", url, headers=headers, data=payload, verify=False, cert=('E:/web学习/华为IOT测试/1_www.ycdemo.cn_bundle.crt', 'E:/web学习/华为IOT测试/2_www.ycdemo.cn.key'))
rdata = json.loads(response.text)
print(rdata['deviceId'])