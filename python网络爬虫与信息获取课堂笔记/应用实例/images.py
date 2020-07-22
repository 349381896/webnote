import requests
import os
url = "https://s1.tuchong.com/content-image/202002/7dcd43685e77534f0b9d2d7c2dbbea1c.png"
image_dir = os.path.join(os.curdir,"static/images")
filename = url.split('/')[-1]
filepath = os.path.join(image_dir,filename)
try:
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    if not os.path.exists(filepath):
        r = requests.get(url)
        with open(filepath,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
