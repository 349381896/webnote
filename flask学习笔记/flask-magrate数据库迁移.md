

1、安装：	
	pip install Flask-Migrate  将模型映射到数据库中

2、配置：	
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
	db = SQLAlchemy(app)
	migrate = Migrate(app, db)	#初始化
			
3、配合flask-script使用：	pip install flask_script

	from flask_migrate import  MigrateCommand
	manager.add_command('db', MigrateCommand)
	
	-指令格式变更为：
		$ python manage.py db init    初始话指令，只能使用一次
		$ python manage.py db migrate  生产迁移文件，内部迁移文件使用链表关联
		$ python manage.py db upgrade  执行迁移文件。更新，升级版本 --message '添加迁移日志'
		$ python manage.py db downgrade 退回旧版本
		$ python manage.py db --help	帮助文档