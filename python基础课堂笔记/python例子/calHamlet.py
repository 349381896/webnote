#英文文本处理
def getText():
    txt = open("python课堂笔记\static\hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '|"#$%&()*+,-./:;<=>?@[\\]^{|}~':
        txt = txt.replace(ch," ")   #将特殊符号替换成空格
    return txt


def main():
    hamlerTxt = getText()
    words = hamlerTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True) #以第二列的元素进行排序，降序
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))

if __name__ == "__main__":
    main()