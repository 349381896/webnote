import requests,json

url = "http://www.ycdemo.cn/api/v2/wxchartgetdata"

payload = {'deviceId': 'ecfbc857-b220-4801-844a-90b353af69e3'}
files = [

]
headers= {'User-Agent':'Labview2018'}

daytiems                 = list()
noise_day10              = []
noise_dayvalue           = []
pm10_day10               = []
humidity_day10           = []
pm10_dayvalue            = []
pm2_day10                = []
pm2_dayvalue             = []
temperature_day10        = []
temperature_dayvalue     = []
tendaytimes              = []


response = requests.request("POST", url, headers=headers, data = payload)
res = json.loads(response.text.encode('utf8'))
daytiems                 = res['daytiems']
humidity_day10           = res['humidity_day10']
humidity_dayvalue        = res['humidity_dayvalue']
noise_day10              = res['noise_day10']
noise_dayvalue           = res['noise_dayvalue']
pm10_day10               = res['pm10_day10']
pm10_dayvalue            = res['pm10_dayvalue']
pm2_day10                = res['pm2_day10']
pm2_dayvalue             = res['pm2_dayvalue']
temperature_day10        = res['temperature_day10']
temperature_dayvalue     = res['temperature_dayvalue']
tendaytimes              = res['tendaytimes']
   

def getdaytime():
     print(daytiems)
     return daytiems   

def get10daytimes():
    return tendaytimes

def getdaypm2():
    return pm2_dayvalue
def getdaypm10():
    return pm10_dayvalue
def getdaytemp():
    return temperature_dayvalue
def getdayhumi():
    return humidity_dayvalue
def getdaynoise():
    return noise_dayvalue

def get10daypm2():
    return pm2_day10
def get10daypm10():
    return pm10_day10
def get10daytemp():
    return temperature_day10
def get10dayhumi():
    return humidity_day10
def get10daynoise():
    return noise_day10

    



getdaytime()

