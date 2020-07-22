# 一、python程序设计思维

## 1、计算思维
- 逻辑思维：推理和演绎，数学为代表
- 实证思维：实验和验证，物理为代表
    - 计算思维：设计和构造，计算机为代表
    - 抽象和自动化
    - 抽象问题的计算过程，利用计算机自动化求解
    - 计算思维时基于计算机的思维

## 2、计算生态于python语言
- 开源思想深入演化和发展，形成了计算生态
- 没有顶层设计、以功能为单位、具备三个特点
    - 竞争发展、相互依存、迅速更迭
- API != 生态
- 编程的起点不是算法而是系统
- 编程如同搭积木，利用计算机生态为主要模式

## 3、用户体验
- 实现功能 -> 用户体验

### 二、基本的程序设计模式
- 确认IPO：明确计算机部分功能边界
- 编写程序：将计算机求解的设计变为现实
- 调试程序：确保程序按照正确的逻辑能够正确运行
- 模块化设计
- 配置化设计
    - 引擎+配置：程序执行和配置分离，将可选参数配置化
    - 将程序开发变成配置文件编写，扩展功能而不修改程序
    - 关键在于接口设计
    - 应用开发的四个步骤
        - 1、产品定义
        - 2、系统架构
        - 3、设计与实现
        - 4、用户体验

# 三、python第三方库的安装
- 方法一：使用pip命令
     - 使用pip需在命令行状态下安装
     - 安装：pip install <第三方库名>  
     - 卸载：pip uninstall <第三方库名> 
     - 下载但不安装：pip download <第三方库名>
     - 第三库详细信息：pip show <第三方库名>  
     - 关键词搜寻第三方库：pip serach <关键词>
     - 列出当前已安装第三方库：pip list

- 方法二：集成安装方法，安装一批的库
    - 使用第三方软件Anaconda:https://www.continuum.io
        - 数据分析的标准平台

- 方法三：文件安装方法
    - 某些第三方库pip下载后，需要编译再安装
    - UCI页面：http://www.ifd.uci.edu/~gohlke/pythonlibs/
        - 提供第三方库编译后的文件
        - 下载后再使用pip安装

# 四、OS库的使用
- os库是python标准库，包含几百哥函数
- 常用路径操作、进程管理、环境参数等几类
    - 路径操作：os.path子库，处理文件路径及信息
    - 进程管理：启动系统中其它程序
    - 环境参数：获得系统软硬件信息等环境参数

## 1、os路径操作
- os.path子库以path为入口，用于操作和处理文件的路径
    - 调用可以如下方式
        - 方法一：
            import os.path
        - 方法二：
            import os.path as op

**os.path子库路径操作函数**
|           函数                            |                         描述                                                                                |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|       os.path.abspath(path)               |   返回path在当前系统中的绝对路径。os.path.abspath("README.txt")。输出："e:\web学习\README.txt"                |
|       os.path.normpath(path)              |   归一化path的表现形式，统一用\\分隔路径。os.path.normpath("D://PYE//file.txt")。输出"D:\\PYE\\file.txt"      |
|       os.path.relpath(path)               |   返回当前程序与文件之间的相对路径（relative path)。os.path.relpath("E:\web学习\python课堂笔记\python例子/test.py")。输出：python课堂笔记\python例子\test.py|
|       os.path.dirname(path)               |   返回path中的目录名称。os.path.dirname("E:\web学习\python课堂笔记\python例子/test.py")。输出：E:\web学习\python课堂笔记\python例子|
|       os.path.basename(path)              |   返回path中最后的文件名。os.path.basename("E:\web学习\python课堂笔记\python例子/test.py")。输出：test.py     |
|       os.path.join(path,*paths)           |   组合path于paths，返回一个路径字符串。os.path.join("D:/","PYE/file.txt")。输出：D:/PYE/file.txt              |
|       os.path.exists(path)                |   判断path对应文件或目录是否存在，返回True或False                                                             |
|       os.path.isfile(path)                |   判断path所对应是否为已存在的文件，返回True或False。os.path.isfile("D://PYE//file.txt")。True                |
|       os.path.isdir(path)                 |   判断path所对应是否为已存在的目录，返回True或False。os.path.isfile("D://PYE//file.txt")。False               |
|       os.path.getatime(path)              |   返回path对应文件或目录上一次的访问时间                                                                      |
|       os.path.getmtime(path)              |   返回path对应文件或目录最近一次的修改时间                                                                    |
|       os.path.getctime(path)              |   返回path对应文件或目录的创建时间                                                                            |
|       os.path.getsize(path)               |   返回path对应文件的大小，以字节为单位                                                                        |

## 2、os的进程管理
- os.system(command)
    - 执行程序或命令command
    - 在windows系统中，返回值为cmd的调用返回信息
    - 参数直接于路径相隔一个空格
    - 举例：
```
print(os.system("C:\\Windows\\System32\\calc.exe"))
输出：0  并调用计算机
```

## 3、os的环境参数
- 获取或改变系统环境信息

|               函数                        |                                   描述                                                                        |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------|
|       os.chidr(path)                      |   修改当前程序操作的路径。os.chdir("D:")                                                                      |
|       os.getcwd()                         |   返回程序当前路径。os.getcwd()。输出：D:\                                                                    |
|       os.curdir                           |   返回当前目录（'.')
|       os.getlogin()                       |   返回当前系统登录用户名称。os.getlogin()。输出：day_day_up                                                   |
|       os.cpu_count()                      |   获取当前系统的cpu数量。os.cpu_count()。输出：4                                                              |
|       os.urandom(n)                       |   获取n个字节长度的随机字符串，通常用于加密运算。os.urandom(10)。输出：b'\xf7\xba\xbc5,\x99\xfd&\x91O'        |
|       os.listdir()                        |   返回指定目录下的所有文件和目录名                                                                            |
|       os.remove()                         |   函数用来删除一个文件                                                                                        |
|       os.removedirs（r“c：\python”）      |   删除多个目录                                                                                                |
|       os.getenv(“HOME”)                   |   读取操作系统环境变量HOME的值                                                                                |
|       os.environ                          |   返回操作系统所有的环境变量                                                                                  |
|       os.environ.setdefault               |   设置系统环境变量，仅程序运行时有效                                                                          |
|       os.linesep                          |   给出当前平台使用的行终止符                                                                                  |
|       os.name                             |   指示你正在使用的平台
|       os.rename（old， new）              |   重命名                                                                                                      |
|       os.makedirs（r“c：\python\test”）   |   创建多级目录                                                                                                |
|       os.mkdir（“test”）                  |   创建单个目录                                                                                                |
|       os.stat（file）                     |   获取文件属性                                                                                                |
|       os.kill(10884,signal.SIGKILL)       |   杀死进程                                                                                                    |


# 五、第三方库安装脚本
- 需求：批量安装第三方库需要人工安装，能否自动安装？
- 自动执行pip逐一根据安装需求安装

|库名	                |           用途                |	pip安装指令             
|-----------------------|-------------------------------|---------------------------
|   NumPy	            |   N维数据表示和运算	        |   pip install numpy       
|   Matplotlib	        |   二维数据可视化	            |   pip install matplotlib
|   PIL	                |   图像处理                    |	pip install pillow
|   Scikit-Learn        |	机器学习和数据挖掘	        |   pip install sklearn
|   Requests	        |   HTTP协议访问及网络爬虫	    |   pip install requests
|   Jieba	            |   中文分词	                |   pip install jieba
|   Beautiful Soup	    |   HTML和XML解析器	            |   pip install beautifulsoup4
|   Wheel	            |   Python第三方库文件打包工具	|   pip install wheel
|   PyInstaller	        |   打包Python源文件为可执行文件|	pip install pyinstaller
|   Django	            |   Python最流行的Web开发框架	|   pip install django
|   Flask	            |   轻量级Web开发框架	        |   pip install flask
|   WeRoBot	            |   微信机器人开发框架	        |   pip install werobot
|   SymPy	            |   数学符号计算工具	        |   pip install sympy
|   Pandas	            |   高效数据分析和计算	        |   pip install pandas
|   Networkx	        |   复杂网络和图结构的建模和分析 |	pip install networkx
|   PyQt5	            |   基于Qt的专业级GUI开发框架	|   pip install pyqt5
|   PyOpenGL	        |   多平台OpenGL开发接口	    |   pip install pyopengl
|   PyPDF2	            |   PDF文件内容提取及处理	    |   pip install pypdf2
|   docopt	            |   Python命令行解析	        |   pip install docopt
|   PyGame	            |   简单小游戏开发框架	        |   pip install pygame