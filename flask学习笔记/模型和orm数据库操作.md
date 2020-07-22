。FLask默认没有提供任何数据库操作的API

。flask可以自己选择数据，用原生语句实现功能，也可以使用ORM：直接操作对象 ，ORM是正对PYTHON语言

	代码利用率低，条件复杂，代码语句长，有很多相似语句是SQL
	在业务逻辑中拼出来的，修改需要了解业务逻辑，直接写SQL容易
	忽视SQL问题
	
		。ORM(Object Relational Mapping)
		。对象关系映射
		。让模型和数据库表产生映射关系
		。操作模型对象就可以使显示数据库的数据操作
		。也是对数据库的隔离
		。可以理解为翻译机

。ORM将对象的操作转化为原生SQL

。优点：
	1、易用性，可以减少重复SQL
	2、性能损耗少
	3、设计灵活，可以轻松实现复杂查询
	4、移植性好

。python的ORM(SQLALChemy)

针对FLASK的支持
 pip install flask-sqlalchemy 
	
	-初始化sqlalchemy: 需要app对象进行初始化
							-懒加载初始
							-db = SQLAlchemy()    db.init_app(app)
							
	-模型定义：继承自db.Model
	
		-设置表名：__tablename__ = 'user'  #表名是字符串类型
		-设置字段: 字段名 = db.Column(db.数据类型，约束）
		-设置外键：字段名 = db.Column(db.数据类型,db.ForeignKey（关联的表面.字段名）
		-为了方便查看对象输出内容,重写repr:
			def __repr__(self):
				return "<User:%s,%s,%s>" % (self.id, self.username,self.password)
		-配置SQLALCHEMY_TRACK_MODIFICATIONS = False 解决警告
		-字段定义：	
			-db.Column
			-字段类型：	
					-数字：Integer | SmallInteger |BIgInteger
					-字符串：String | Text | Unicode |UnicodeText
					-时间： Date | Time | DateTime
			-字段约束：
				========================================================
				|-primary_key   - 若为True,这列就是表的主键            |
				|-autoincrement - 若为true,则自增                      |
				|-unique        - 若为True,这列不允许出现重复的值      |
				|-default       - 若为True,这列允许为null              |
				|-nullable      - 若为True,这列允许为null              |
				|-index         - 若为True,为这列创建索引,提升查询效率 |
				|-ForeignKey    - 设置外键                             |
				=======================================================
					
				Flask-SQLAlchemy要求每个模型都要定义主键，这一列常被命名为id。
				虽然没有强制要求，但为一般会为模型定义一个 __repr__() 方法，
				返回一个具有可读性的字符串模型（和__str__()类似），可在调试和测试时使用
			-外键约束：
				关系型数据库有个非常重要的概念就是外键约束。
				那么在 Flask-SQLAlchemy 中怎么指定外键约束呢?
				class Article(db.Model):
					author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
		||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||			
		|	-反向引用：                                                                |
		|	Flask-SQLAlchemy 中还提供了一种反向引用的关系。                            |
		|	反向引用可以根据外键约束找到关联的关系模型，                               |
		|	此时可以直接获取相关的模型对象，而不是外键的值。                           |
		|                                                                              |
		|		class User(db.Model):                                                  |
		|			# ...                                                              |
		|			xxx = db.relationship('Article', backref='user')                   |
		|		                                                                       |
		|		class Article(db.Model):                                               |
		|			# ...                                                              |
		|			yyy = db.relationship('User', backref='articles')                  |
		||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||                                                                              |
		|		这是干了个什么事儿呢？假设有如下代码:                                  |
		|                                                                              |
		|			user = User(username="flask")                                      |
		|			db.session.add(user)                                               |
		|			db.session.commit()                                                |
		|			                                                                   |
		|			art1 = Article(title="title1", content="text1", author_id=user.id) |
		|			art2 = Article(title="title2", content="text2", author_id=user.id) |
		|			db.session.add(art1)                                               |
		|			db.session.add(art2)                                               |
		|			db.session.commit()                                                |
		|			                                                                   |
		|	下面看看这个是怎么用的：                                                   |
		|	可以很明显猜到是 xxx = db.relationship('Article', backref='user') 和       |
		|yyy = db.relationship('User', backref='articles') 这两句起的作用，            |
		|分析下它们的共性，我们就能看明白反向引用的用法了。首先这里是随便定义了一      |
		|个成员 xxx, yyy 这里想说的是，这里随便定义什么都不影响，这里只是举例告诉      |
		|你不影响，所以随便取了名字，你以后在写的时候，最好不要这样，最好定义一些      |
		|有意义的名字。其次就是两个参数，第一个参数，不难发现，是和本表有外键约束      |
		|的那个表的模型名(类名)而不是前面说的那样的是表名(__tablename__)。第二个       |
		|参数，也还好理解，其实就是我们在进行反向引用时使用的那个变量。我们在user      |
		|表中加入了 articles 这个反向引用，我们就可以通过 u.articles 得到这个用户      |
		|的所有article。同样，我们在article表中加入了 user 这个反向引用，我们就可以    |
		|通过 art.user 得到这个art的user。                                             |
		||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
			
			
			
			

	-创建表：db.create_all()
	-删除表：db.drop_all()


。数据库链接：dialect + driver://username:password@host:port/database
	-dialect数据库实现
	-driver数据库的驱动
	-username
	-password
	-host
	-port
	-database
	-使用sqlite数据库举例：sqlite:////tmp/test.db 	
  
 
	-创建数据库：
		·为了创建初始数据库，只需要从交互式 Python shell 中导入 db 对象并且调用 SQLAlchemy.create_all()（db.create_all()）方法来创建表和数据库;删除数据库db.drop_all()
	-添加用户：
		·	>>> db.session.add(admin)
			>>> db.session.add(guest)  
			>>> db.session.add_all(list[object])
			>>> db.session.commit()
			
			-例程：
						students = []
						for i in range(10):
							student = Students()
							student.s_name = '小学生%d号'% random.randrange(100)
							students.append(student)
						db.session.add_all(students)
						db.session.commit()
			
			
	-删除用户：
			>>> db.session.delete(object)
			
			-例程：
				student = Students.query.filter_by(s_name='肖春明').first()
    
				db.session.delete(student)
				db.session.commit()
	-查询数据库：
		·   users = User.query.all()
		
		-常用执行过滤器:
		========================================================================
		|		方法			|		说明                                    |
		|-----------------------|-----------------------------------------------|
		|		all()			|	以列表形式返回查询的所有结果                |
		|		first()			|	返回查询的第一个结果，如果未查到，返回None  |
		|		first_or_404()	|	返回查询的第一个结果，如果未查到，返回404   |
		|		get()			|	返回指定主键对应的行，如不存在，返回None    |
		|		get_or_404()	|	返回指定主键对应的行，如不存在，返回404     |
		|		count()			|	返回查询结果的数量                          |
		|		paginate()		|	返回一个Paginate对象，它包含指定范围内的结果|
		========================================================================
		
		-.常用查询过滤器:
		=========================================================================
		|	过滤器			|			说明                                    |
		|-------------------|---------------------------------------------------|
		|	filter()	  	|	把过滤器添加到原查询上，返回一个新查询          |
		|	filter_by()		|	把等值过滤器添加到原查询上，返回一个新查询      |
		|	limit			|	使用指定的值限定原查询返回的结果                |
		|	offset()		|	偏移原查询返回的结果，返回一个新查询            |
		|	order_by()		|	根据指定条件对原查询结果进行排序，返回一个新查询|
		|	group_by()		|	根据指定条件对原查询结果进行分组，返回一个新查询|
		=========================================================================
							
									
	-修改数据库：
		无专门用的语句，修改需要先查询再幅值再提交。
		
		-例程：
				student = Students.query.filter_by(s_name='肖春明').first()
				student.s_name = 'lallalla'
				db.session.add(student)
				db.session.commit()
				
	-移除会话：db.session.remove()


#### 项目结构
- manage.py         用来控制程序的
- App/__init__       初始化文件
    - 初始化整个Flask对象，以及Flask所用的各种插件
- App/settings
    - 配置整个项目运行环境
- App/ext
    - 项目的扩展库
    - 第三方扩展库打包处理
- App/views 
    - 视图函数
    - 协调业务逻辑
    - 协调模板和模型之间的关系
- App/modes
    - 模型
    - 定义模型结构
    - 获得数据库中的表的关系映射

