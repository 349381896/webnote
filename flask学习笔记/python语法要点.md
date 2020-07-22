
1、参数形式:
	- *args 用来将参数打包成tuple给函数体调用
	- **kwargs 打包关键字参数成dict给函数体调用
	
	
2、多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来

3、split()函数
	描述：拆分字符串。通过指定分隔符sep对字符串进行分割，并返回分割后的字符串列表

	语法：	 str.split(sep=None, maxsplit=-1)  -> list of strings  返回 字符串列表 
			 或str.split(sep=None, maxsplit=-1)[n]  

		sep —— 分隔符，默认为空格,但不能为空即(")。
		maxsplit —— 最大分割参数，默认参数为-1。
		[n] —— 返回列表中下标为n的元素。列表索引的用法
		
	单一分隔符，str.split()与 re.split()效果是一样的
	多个单一 分隔符 时 ，”[]”与 “|”的 效果是一样的，但是 请注意 使用 “|”时某些字符 
	需要转义多个长短不一的的分隔符的分隔符时，就应该使用 “|”适用 “（）”则是 将分隔
	后的结果保留分隔符（在split中，分隔符理应是被刨除的，所以这里有点难理解）

4、json.dumps(data)=>字典转字符串
   json.loads(data)=>字符串转字典
   
5、random函数的用法
	# -*- coding: UTF-8 -*-

	import random
	import string

	# 随机整数：
	print random.randint(1,50)

	# 随机选取0到100间的偶数：
	print random.randrange(0, 101, 2)

	# 随机浮点数：
	print random.random()
	print random.uniform(1, 10)

	# 随机字符：
	print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')

	# 多个字符中生成指定数量的随机字符：
	print random.sample('zyxwvutsrqponmlkjihgfedcba',5)

	# 从a-zA-Z0-9生成指定数量的随机字符：
	ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
	print ran_str

	# 多个字符中选取指定数量的字符组成新字符串：
	print ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))

	# 随机选取字符串：
	print random.choice(['剪刀', '石头', '布'])

	# 打乱排序
	items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	print random.shuffle(items)


