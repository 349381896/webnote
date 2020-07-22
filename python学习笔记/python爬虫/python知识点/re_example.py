import re
text = ''
file = open('F:\python学习笔记\python爬虫\python知识点\poem.txt') #打开文本
for line in file:
    text =  text + line
file.close()

"""
result = re.findall(' (a[a-z][a-z]) |(A[a-z][a-z])',text)  #在全文中找
# result = set(result)        #去除重复的内容
final_result = set()
for pair in result:
    if pair[0] not in final_result:
        final_result.add(pair[0])
    if pair[1] not in final_result:
        final_result.add(pair[1])
final_result.remove('') #去掉空的元素
print(final_result)

"""

result = re.findall('\w+',text)  #\d表示数字  +至少要有一个数
print(result)