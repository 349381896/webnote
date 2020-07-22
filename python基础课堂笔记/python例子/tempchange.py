#
temp = input("请输入")
if temp[-1] in ["F","f"]:
    hTemp = (eval(temp[0:-1])-32)/1.8
    print("温度{:.2f}C".format(hTemp))
elif temp[-1] in ["C","c"]:
    cTemp = eval(temp[0:-1])*1.8 +32
    print("温度{:.2f}F".format(cTemp))
else:
    print("输入格式错误")