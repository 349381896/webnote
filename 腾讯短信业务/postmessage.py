from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile # 导入可选配置类
from tencentcloud.common.profile.http_profile import HttpProfile # 导入可选配置类
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.sms.v20190711 import sms_client, models # 导入 SMS 模块的client models
import json
try: 
     # 必要步骤：
    # 实例化一个认证对象，入参需要传入腾讯云账户密钥对 secretId 和 secretKey
    # 本示例采用从环境变量读取的方式，需要预先在环境变量中设置这两个值
    # 您也可以直接在代码中写入密钥对，但需谨防泄露，不要将代码复制、上传或者分享给他人
    # CAM 密钥查询：https://console.cloud.tencent.com/cam/capi
    cred = credential.Credential("AKIDVnpLfjH8RTnzXnAu4ybyA2VkjRt4nsY9", "YppY16zdAQPcYEdngIfm9FeIriCQFwQ1") 
    
    # 实例化一个 http 选项，可选，无特殊需求时可以跳过
    httpProfile = HttpProfile() 
    httpProfile.endpoint = "sms.tencentcloudapi.com" # 指定接入地域域名（默认就近接入）

    # 非必要步骤:
    # 实例化一个客户端配置对象，可以指定超时时间等配置
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    # 实例化 SMS 的 client 对象
    # 第二个参数是地域信息，可以直接填写字符串 ap-guangzhou，或者引用预设的常量
    client = sms_client.SmsClient(cred, "ap-guangzhou", clientProfile) 

    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    # 您可以直接查询 SDK 源码确定 SendSmsRequest 有哪些属性可以设置
    # 属性可能是基本类型，也可能引用了另一个数据结构
    # 推荐使用 IDE 进行开发，可以方便的跳转查阅各个接口和数据结构的文档说明
    req = models.SendSmsRequest()
    params = '''{
        "PhoneNumberSet":["+8618270791551"],
        "TemplateID":"659819",
        "Sign":"扬尘监控小能手",
        "TemplateParamSet":["1","93","轻度污染"],
        "SmsSdkAppid":"1400398349"
        }'''
    params = json.loads(params)
    params['PhoneNumberSet']=["+8618270791551","+8615297712025"]
    params['TemplateParamSet'] = ["1","100","轻度污染"]
    params = json.dumps(params)
    req.from_json_string(params)
    resp = client.SendSms(req) #发起请求
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err)