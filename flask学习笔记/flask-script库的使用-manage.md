1、安装flask-script模块
	pip install flask-script
	
2、创建对象：
	manager = Manager(app)
 - 
3、启动代码：
	if __name__ == '__main__':
		manager.run()
		
4、启动参数说明：
	-h, --host   	指定主机
	-p, --port   	指定端口
	-d         		开启调试模式
	-r        		代码修改后自动加载
	-?, --help    	查看帮助信
	
5、终端启动：python manage.py runserver -d -r -h 0.0.0.0 -p 5000