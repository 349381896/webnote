
==================参数:====================
1、路径参数
	。 位置参数
	。 关键参数
2、请求参数
	。 get参数在路径中？之后
	。 post参数在请求体Body

=================Flask中参数：================
	。 都是关键字参数
	。 默认标识是尖括号<name>
	。 name 需要和对应的视图函数的参数名字保持一致
	。 参数允许有默认值
		- 如果有默认值，那么在路由中，不传输参数也是允许的
		- 如果没有默认值，参数在路由中必须传递
	。 默认参数类型是字符串
	。 参数语法<converter:var>
		- converter类型
		- string 前面所说的默认，会将斜线认为参数分割符
		- int 
		- float
		- path 接收到的数据格式是字符串，特性会将斜线认为是一个字符
		- uuid限制参数
		- any 限制参数为给定的值'/<any(x,y,z):var>。var只能为x,y,z中的一个
			· 和枚举是一回事
	。 请求方法
		- 请求方法并不是像djiango一样，全部支持
		- 需要自己手动配置请求方法
			· methods=['GET','POST','DELETE']
		-请求工具
			· postman
			· httpie
	。 反向解析
		- url_for 根据endpoint获取对应的路径
		- endpoint默认就是函数的名字
		- 如果有参数 url_for('函数名'，key=value,key=value)
		- 反向解析可以在模板中直接使用
