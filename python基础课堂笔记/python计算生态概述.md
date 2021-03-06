# 一、从数据间处理到人工智能
数据表示 -> 数据清洗 -> 数据统计 -> 数据可似化 -> 数据挖掘 -> 人工智能
    -数据表示：采用合适方式用程序表达数据
    -数据清洗：数据归一化，数据转换，异常处理
    -数据统计：数据的概要理解，数量、分布、中位数
    -数据可视化：直观展示数据内涵的方式
    -数据挖掘：从数据分析获得知识，产生数据外的价值
    -人工智能：数据/语言/图像/视觉等方面升读分析与决策

## 1、python库之数据分析
    -Numpy:表达N维数组的最基础库
        -python接口使用，c语言实现，计算速度优异
        -Python数据分析及科学计算的基础库，支撑Pandas等
        -提供直接的矩阵运算，广播函数、线性代数等功能

    -Pandas:python数据分析高层次应用库
        -提供了简单易用的数据结构和数据分析工具
        -理解数据类型与索引的关系，操作索引即操作数据
        -python最主要的数据分析功能库，基于Numpy开发
        -Series = 索引 + 一位数据
        -DataFrame = 行列索引 + 二维数据

    -SciPy：数学、科学和工程计算功能库
        -提供了一批数学算法及工程数据运算功能
        -类似Matlab,可用于如傅里叶变换，信号处理等应用
        -Python最主要的科学计算功能库，基于Numpy开发

## 2、python库之数据可视化
    -Matplotlib:高质量的二维数据可视化功能库
        -提供超过100种的数据可视化展示效果
        -通过matplotlib.pyplot子库调用各种可视化效果
        -python最主要的数据可视化功能库，基于Numpy开发

    -Seaborn:统计类数据可视化功能库
        -提供了一批高层次的统计类数据的可视化展示效果
        -主要展示数据间分布，分类和线性关系等内容
        -基于Matplotlib开发，支持Numpy和Pandas

    -Mayavi:三维科学数据可视化功能库
        -提供一批简单易用的3D科学计算数据可视化展示效果
        -目前版本Mayavi2,三维可视化主主要的第三方库
        -支持Numpy、TVTK、Traits、Envisage等第三方库

## 3、python库之文本处理
    -PyPDF2:用于处理pdf文件的工具集
        -提供了一批处理PDF文件的计算功能
        -支持获取信息、分隔/整合文件，加密解密等
        -完全Python语言实现，不需要额外依赖，功能稳定

    -NLTK:自然语言文本处理第三方库
        -提供了一批简单易用的自然语言文本处理功能
        -支持语言文本类型、标记、语法句法、语义分析
        -最优秀的python自然语言处理处理库

    -Python-docx:创建或更新Microsoft Word文件的第三方库
        -提供创建或更新.doc等文件的计算功能
        -增加并配置段落、图片、表格、文件等，功能全面

## 3、python库之机器学习
    -Scikit-learn:机器学习方法工具集
        -提供一批统一化的机器学习方法功能接口
        -提供聚类、分类、回归、强化等计算功能
        -机器学习最基本且最优秀的Python第三方库

    -TensorFlow:AlphaGo背后的机器学习计算框架
        -谷歌公司推动的开源机器学习框架
        -将数据流图为基础，图片节点代表运算，边代表张量
        -应用机器学习方法的一种方式，支撑谷歌人工智能引应用

    -MXNet:基于神经网络的深度学习计算框架
        -提供可扩展的神经网络及深度学习计算功能
        -可用于自动驾驶、机器翻译、语音识别等众多领域
        -python最重要的深度学习框架

# 二、从web解析到网络空间

## 1、python库之网络爬虫
    -Request:最友好的网络爬虫功能库
        -提供了简单易用的类HTTP协议网络爬虫
        -支持连接池、SSL、Cookies、HTTP(s)代理等
        -Python最主要的页面网络爬虫功能库

    -Scrapy:优秀的网络爬虫框架
        -提供了构建网络爬虫系统的框架功能，功能半成品
        -支持批量和定时网页爬取、提供数据处理流程等
        -python最主要且最专业的网络爬虫框架

    -pyspider:强大的web页面爬虫系统
        -提供数据库后端、消息队列、优先级、分布式架构等
        -提供了完整的网页爬取系统构建功能
        -python重要的网络爬虫类第三方库

## 2、python库之web信息提取
    -Beautiful Soup:HTML和XML的解析库
        -提供了解析HTML和XML等web信息的功能
        -又名beautifulsoup4或bs4,可以加载多种解析引擎
        -常与网络爬虫库搭配使用，如Scrapy、request等

    -Re:正则表达式解析和处理功能库
        -提供了定义和解析正则表达式的一批通用功能
        -可用于各类场景，包括定点的web信息提取
        -python最重要的标准库之一，无需安装

    -Python-Goose:提取文章类型web页面的功能库
        -提供了对web页面中文章信息/视频等元数据的提取功能
        -针对特定类型的web页面，应用覆盖面较广
        -python最主要的web信息提取库

## 3、python库之web网站开发
    -Django:最流行的web应用框架
        -提供了构建web系统的基本应用框架
        -MTV模式：模型、模板、视图
        -python最重要的web应用框架，略微复杂的应用框架

    -Pyramid:规模适中的web应用框架
        -提供了简单方便构建web系统的应用框架
        -不大不小，规模适中，适合快速构建并适度扩展类应用
        -python产品级web应用框架，起步简单可扩展性好

    -Flask：web应用开发微框架
        -提供了最简单构建web系统的应用框架
        -特点是：简单、规模小、快速

## 4、python库之网络应用开发
    -WeRoBot:微信公众号开发框架
        -提供了解析微信服务器服务器消息及反馈消息的功能
        -建立微信机器人的重要技术手段

    -aip:百度AI开放平台接口
        -提供了访问百度AI服务的python功能接口
        -语音、人脸、OCR、NLP、知识图谱、图像搜索等领域
        -python百度AI应用的最主要方式

    -MyQR:二维码生成的第三方库
        -提供了生成二维码的系列功能
        -基本二维码、艺术二维码和动态二维码

# 三、从人机交互到艺术设计

## 1、python库之图形用户界面
    -PyQt5:Qt开发框架的python接口
        -提供了创建Qt5程序的python api接口
        -Qt是非常成熟的跨平台桌面应用开发系统，完备GUI
        -推荐的python GUI开发第三方库

    -wxPython:跨平台GUI开发框架
        -提供了专用于python的跨平台GUI开发框架
        -理解数据类型与索引的关系，操作索引即操作数据
        -python最主要的数据分析功能库，基于Numpy开发
    
    -PyGObject:使用GTK+开发GUI的功能库
        -提供了整合GTK+、WebkitGTK+等库的功能
        -GTK+:跨平台的一种用户图形界面GUI框架
        -实例:Anaconda采用该库构建GUI


## 2、python库之游戏开发
    -PyGame：简单的游戏开发功能库

    -Panda3D:开源、跨平台的3D渲染和游戏开发库
        -一个3D游戏引擎，提供python和C++两种接口
        -支持很多先进特性：法线贴图、光泽贴图、卡通渲染等
        -由迪士尼和卡尼基梅隆大学共同开发
    
    -cocos2d:构建2D游戏和图形界面交互式应用的框架
        -提供了基于OpenGL的游戏开发图形渲染功能
        -支持GPU加速，采用树形结构分层管理游戏对象类型
        -适用于2d专业游戏开发

## 3、python库之虚拟现实
    -VR Zero:在树莓派上开发VR应用的Python库
        -提供大量与VR开发相关的功能
        -针对树莓派的VR开发库，支持设备小型化，配置简单化
        -非常适合初学者实践VR开发及应用
    
    -pyovr:Ovulus Rift的python开发接口
        -针对Oculus VR设备的python开方库
        -基于成熟的VR设备，提供全套文档，工业应用设备
        -python+虚拟现实领域探索的一种思路

    -Vizard:基于python的通用VR开发库

## 4、Python库之图形艺术
    -Quads:迭代的艺术
        -对图片进行四分迭代，形成像素风
        -可以生成动图或静图图像
        -简单易用，具有很高展示图

    -ascii_art:ASCII艺术库
        -将普通图片转为ASCII艺术风格
        -输出可以是纯文本或彩色文本
        -可以采用图片格式输出
    
    -turtle库