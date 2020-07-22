1、request:

	。 属性
		- data 	 : 	记录请求的数据，并转化为字符串
		- form 	 : 	记录请求中的表单数据，就是body中的内容，一般是POST中的请求
		- args 	 : 	记录请求中的查询参数，一般是？key=value&key1=value2 的形式。是GET的参数
		- cookies: 	记录请求中的cookies信息
		- headers: 	记录请求中的报文头
		- method :   记录请求中使用的HTTP方法
		- url	 :	记录请求的Url地址
		- files  :	记录请求中上传的文件
		- json	 ： 可以使用这个替代get_json()方法

	。 获取字典中的数据（如获取GET和POST的参数），可以使用get或getlist方法,前者是获取第一个符合参数，后者是列出所有符合参数。提取文件数据后，可以用.save方法存储。

	。 http请求方法
		GET    ： 	从指定的资源请求数据
		POST   : 	向指定的资源提交要被处理的数据
		HEAD   : 	与GET相同，但只返回HTTP报头，不返回文档主体
		PUT    : 	上传指定的URL表示
		DELETE :	删除指定资源
		OPTIONS:	返回服务器的HTTP方法
		CONNECT:	把请求连接转换到透明的TCP/IP通道
		
	- GET方法的参数在args中：request.args.get('username')
	- POST方法的上传数据在form表单中：request.form.get('username')    存储格式是dict
	- 字典的值可以通过request.form['username']  #其中username是key值
	
	
		
		
		
		
		
		
		
		
		
		
		

2、response: ctry+p显示函数输入参数 ctry+d复制 ctry+b进入源码

	。 视图函数返回接收两种类型
		-Response对象
		-字符串
			·针对字符串flask会帮我们包装成Response
	。 返回内容
		-返回的字符串
			·render_template
			·添加第二个参数，可以控制返回状态码
				·数据正常，返回错误的状态码，干扰爬虫
			·make_response
				·制作一个响应进行返回
			·Response
				·直接创建Response进行返回
			·其实最终返回的都是Response对象
			·返回JSON
				·json.jsonify将数据格式转换为json格式，同时设置返回类型为application/json
				·json.dumps将数据转化为json格式，没有设置返回类型，默认为字符串
				
				.json.dumps(data)=>字典转字符串
				.json.loads(data)=>字符串转字典
	
3、爬虫：

	。 数据获取->数据提取->数据存储 

4、 redirect重定向 : redirect(url_for('hello_world'))



	
