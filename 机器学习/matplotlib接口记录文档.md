# matplotlib库一些常用属性和方法记录（自用）——可与seaborn库搭配使用获取更好的绘图效果
> import matplotlib.pyplot as plt #pyplot是matplotlib中二维绘制的库

## 1.首先创建Figure对象
>figure(num,figsize,dpi,facecolor,edgecolor,frameon)

|       参数            |       说明                                        |
|-----------------------|---------------------------------------------------|
|       num             |图形的编号或名称，取值为数字或字符串
|       figsize         |绘制对象的宽和高，单位是英寸，figsize=(3,2)
|       dpi             |绘制对象的分辨率，缺省值为80
|       facecolor       |背景颜色
|       edgecolor       |边框颜色
|       frameon         |表示是否显示边框
```
plt.figure(figsize=(3,4),facecolor='g')
plt.plot()
plt.show()
```

#### 1.1 figure对象--划分子图
> .subplot(行数,列数,子图序列)
```
def subplots_adjust(self, left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)#手动调整子图之间的间隔
	'''
	left = 0.125  # the left side of the subplots of the figure
	right = 0.9   # the right side of the subplots of the figure
	bottom = 0.1  # the bottom of the subplots of the figure
	top = 0.9     # the top of the subplots of the figure
	wspace = 0.2  # the amount of width reserved for space between subplots,
	              # expressed as a fraction of the average axis width
	hspace = 0.2  # the amount of height reserved for space between subplots,
	              # expressed as a fraction of the average axis height
	'''
```
>plt.tight_layout(rect=[left,bottom,right,top])  #自动调整间隔，左，下，右，上在画布的范围

## 2.绘图标注
### 2.1 中文字体
|       方法            |       说明                                        |
|-----------------------|---------------------------------------------------|
|   plt.rcParams["font.sans-serif"]="SimHei"|设置字体文中文黑体
|   plt.rcdefaults()    |恢复标准默认配置

### 2.2 标题
|       方法            |       说明                                        |
|-----------------------|---------------------------------------------------|
|   plt.suptitle()      |添加全局标题
|   plt.title()         |添加子标题

#### 2.2.1 plt.suptitle()全局标题函数的主要标题
|       参数            |       说明                                        |   默认值
|-----------------------|---------------------------------------------------|-----------|
|       x               |标题位置的x坐标                                    |   0.5
|       y               |标题位置的y坐标                                    |   0，98
|       color           |标题颜色                                           |   黑色
|       backgroundcolor |标题背景颜色                                       |   12
|       fontsize        |标题的字体大小                                     |   
|       fontweight      |字体粗细                                           |   normal
|       fontstyle       |设置字体类型                                       |   
|    hrizontalalignment |标题水平对齐方式                                   |   center
|    verticalalignment  |标题的垂直对齐方式                                 |   top

#### 2.2.2 plt.title()子标题函数的主要标题
|       参数            |       说明                                        |   取值
|-----------------------|---------------------------------------------------|-----------|
|       loc             |标题位置                                           |   left,right
|       rotation        |标题文字旋转的角度                                 |   
|       color           |标题颜色                                           |   黑色
|       fontsize        |标题的字体大小                                     |   
|       fontweight      |字体粗细                                           |   normal
|       fontstyle       |设置字体类型                                       |   
|    hrizontalalignment |标题水平对齐方式                                   |   center
|    verticalalignment  |标题的垂直对齐方式                                 |   top
|       fontdict        |设置参数字典

#### 2.3 plt.text(x,y,s,fontsize,color)文字添加函数
|       参数            |       说明                                        |   默认值
|-----------------------|---------------------------------------------------|-----------|
|       x               |文字的x坐标                                        |   不可省略
|       y               |文字的y坐标                                        |   不可省略
|       color           |文字的颜色                                         |   黑色
|       fontsize        |文字的大小                                         |   12
|       s               |显示的文字                                         |   不可省略  

#### 2.4 坐标轴的设置
>plt.rcParams["axes.unicode_minus"] = False#解决坐标轴负号显示问题

|       方法            |       说明                                        |
|-----------------------|---------------------------------------------------|
|   plt.xlabel(x,y,s,fontsize,color)    |   设置x轴标签
|   plt.ylabel(x,y,s,fontsize,color)    |   设置y轴标签
|   plt.xlim(xmin,xmax)                 |   设置x轴坐标的范围
|   plt.ylim(ymin.ymax)                 |   设置y轴坐标的范围
|   plt.tick_params(labelsize)          |   设置刻度文字的字号
|	plt.axis('off')						|	关闭坐标轴

## 3、散点图(Scatter)的绘制
**plt.scatter(x,y,scale,color,marker,label,c,cmap)**
|       参数            |       说明                                        | 默认值    | 
|-----------------------|---------------------------------------------------|-----------|
|       x               |数据点的x坐标，通常数列表                          |   不可省略
|       y               |数据点的y坐标，通常数列表                          |   不可省略
|       scale           |数据点的大小                                       |   36
|       color           |数据点的颜色										|  可以是一个颜色序列rbg
|       marker          |数据点的样式                                       |   'o'
|       label           |图例文字											|
|		c				|色彩映射的依据序列
|		cmap			|色彩映射中的颜色
>设置图例后，需要使用plt.legend(loc,fontsize)在当前子图中显示；loc=0-10

==数据点样式可选：==
|      样式            |       说明                                        |
|-----------------------|---------------------------------------------------|
|       ‘.’             |        点(point marker)
|       ‘,’             |        像素点(pixel marker)
|       ‘o’             |        圆形(circle marker)
|       ‘v’             |        朝下三角形(triangle_down marker)
|       ‘^’             |        朝上三角形(triangle_up marker)
|       ‘<‘             |        朝左三角形(triangle_left marker)
|       ‘>’             |        朝右三角形(triangle_right marker)
|       ‘1’             |        (tri_down marker)
|       ‘2’             |        (tri_up marker)
|       ‘3’             |        (tri_left marker)
|       ‘4’             |        (tri_right marker)
|       ‘s’             |        正方形(square marker)
|       ‘p’             |        五边星(pentagon marker)
|       ‘*’             |        星型(star marker)
|       ‘h’             |        1号六角形(hexagon1 marker)
|       ‘H’             |        2号六角形(hexagon2 marker)
|       ‘+’             |        +号标记(plus marker)
|       ‘x’             |        x号标记(x marker)
|       ‘D’             |        菱形(diamond marker)
|       ‘d’             |        小型菱形(thin_diamond marker)
|       ‘|’             |        垂直线形(vline marker)
|       ‘_’             |        水平线形(hline marker)

## 4、折线图(line Chart)的绘制
**plt.plot(x,y,color,marker,label,linewidth,markersize)**
|       参数            |       说明                                        |   默认值
|-----------------------|---------------------------------------------------|-----------|
|       x               |数据点的x坐标                                      |   0,1,2...
|       y               |数据点的y坐标                                      |   不可省略
|       color           |折线颜色                                           |   
|       marker          |数据点的样式                                       |   'o'
|       label           |图例文字
|       linewidth       |折线图的宽度
|       markersize      |数据点的大小

## 4、柱形图(Bar Chart)的绘制
**plt.bar(left,height,width,facecolor,edgecolor,label)**
|       参数            |       说明                                        | 
|-----------------------|---------------------------------------------------|
| left                  |x轴的位置序列，一般采用range函数产生一个序列，但是有时候可以是字符串
| height                |y轴的数值序列，也就是柱形图的高度，一般就是我们需要展示的数据；
| alpha                 |透明度，值越小越透明
| width                 |为柱形图的宽度，一般这是为0.8即可；
| color或facecolor      |柱形图填充的颜色；
| edgecolor             |图形边缘颜色
| label                 |图例文字

## 5.图像显示
- plt.imshow(image对象/Numpy数组,cmap)
>cmap:显示模式如gray

```
plt.figure(figsize=(5,5))
plt.imshow(image)
olt.show()
```
