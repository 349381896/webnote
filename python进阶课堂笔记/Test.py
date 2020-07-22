class A(object):
    name ='zs'
    def test1(self):
        print('.........A 的test1方法') #对象方法

    @classmethod    #声明下面方法为类方法，类方法前一定要加修饰器，类方法的参数cls,代表当前的类
    def test2(cls):
        cls.name = 'ls' #修改类属性
        print('.........A 的test2方法')

a = A()
a.test2()
a.test1()
A.test2() #调用类方法
print(A.name)