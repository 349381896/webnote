#基本统计值计算

def getNum():
    nums = []
    iNumStr = input("请输入数字(回车退出)：")
    while iNumStr !="":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出)：")
    return nums

def mean(numbers):  #计算平均值
    s = 0.0
    for num in numbers:
        s += num
    return s/len(numbers)

def dev(numbers,mean):#计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev/(len(numbers)-1),0.5)

def median(numbers):    #中位数
    sorted(numbers)
    size = len(numbers)
    if  size%2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med


def main():
    n = getNum()
    m = mean(n)
    print(m,dev(n,m),median)

if __name__ == "__main__":
    main()