# Numpy库一些常用属性和方法记录（自用）
>import numpy as np

## 1、numpy创建方法介绍
### 1.1 基础数组创建
|   方法                |       说明                                        |
|-----------------------|-----------------------------------------------------|
|   np.array(x)         |将输入数据转化为一个ndarray的数组
|   np.array(x, dtype) |将输入数据转化为一个类型为type的ndarray:np.int64
|   np.asarray(array)   |将列表或元组转化为数组对象
|   np.reshape(shape)   |不改变当前数组，按照shape创建新的数组
|   np.resize(shape)    |改变当前数组，按照shape创建数组
>当数据源本身已经是一个ndarray对象时，array()仍然会复制出一个副本，而asarray()则直接引用了本来的数组

### 1.2 ndarray的元素类型
|   数据类型            |                   说明
|-----------------------|----------------------------------------------------------|
|   bool                |   布尔类型，True或False
|   intc                |   与c语言中的int类型一致，一般是int32或int64
|   intp                |   用于索引的整数，与c语言中ssize_t一致，int32或int64
|   int8                |   字节长度的整数，取值：[-128,127]    
|   int16               |   16位长度的整数，取值：[-32768,32767]
|   int32               |   32位长度的整数，取值：[-2^31 ,2^31-1]
|   int64               |   64位长度的整数，取值：[-2^63 ,2^63-1]
|   uint8               |   8位无符号整数，取值：[0,255]
|   uint16              |   16位无符号整数
|   uint32              |   32位无符号整数
|   uint64              |   64位无符号整数
|   float16             |   16位半精度浮点数：1位符号位，5位指数，10位尾数
|   float32             |   32位半精度浮点数：1位符号位，8位指数，23位尾数
|   float64             |   64位半精度浮点数：1位符号位，11位指数，52位尾数
|   complex64           |   复数类型，实部和虚部都是32位浮点数
|   complex128          |   复数类型，实部和虚部都是32位浮点数

**ndarray对象操作**
|   方法                |       说明                                        |
|-----------------------|-----------------------------------------------------|
|ndarray.mean( axis=0 )	   |     求平均值 
|ndarray.sum( axis= 0)	   |     求和 
|ndarray.cumsum( axis=0)   |     累加 
|ndarray.cumprod( axis=0)  |     累乘
|ndarray.std()             |     方差
|ndarray.var()             |     标准差
|ndarray.max()             |     最大值
|ndarray.min()             |     最小值
|ndarray.argmax()          |     最大值索引
|ndarray.argmin()          |     最小值索引
|ndarray.any()             |     是否至少有一个True
|ndarray.all()             |     是否全部为True
|ndarray.dot( ndarray)     |     计算矩阵内积

### 1.3 ndarray与matrix对象的属性
|   属性                |                   说明
|-----------------------|--------------------------------------------------
|   .ndim               |   秩，即轴的数量或维度的数量
|   .shape              |   ndarray对象的尺度，对于矩阵，n行m列
|   .size               |   ndarray对象元素的个数，相当于.shape中n*m的值
|   .dtype              |   ndarray对象的元素类型
|   .itemsize           |   ndarray对象中每个元素的大小，以字节为单位
|   .T	                |   简单转置矩阵ndarray
|   .I                  |   矩阵求逆
### 1.4 创建特殊数组
|   方法                |       说明                                        |
|-----------------------|-----------------------------------------------------|
|   np.arange(begin,end,step，dtype)|创建数字序列可以有 
|   np.ones(shape,dtype)  |生成一个shape形状的全一ndarray,dtype为可选参数
|   np.ones_like(ndarray)|生成一个形状与参数相同的全一ndarray
|   np.zeros(shape,dtype)  |生成一个shape形状的一维全零ndarray,dtype可选参数
|   np.zeros_like(ndarray)|类似np.ones_like( ndarray )
|   np.eye(shape)       |创建一个shape形状的单位矩阵（对角线为1，其余为0）
|   np.linspace(start,stop,num=5) |创建等差数列
|   np.logspace(start,stop,num=5,base=10)  |创建等比数列10^start ->10^stop

### 1.5 矩阵创建
|   方法                |       说明                                        |
|-----------------------|-----------------------------------------------------
| np.matrix(str/list/tuble/array)|创建字符串/列表/元组/数组的矩阵
| np.mat()              |与matrix一致
>matrix矩阵的属性与ndarray一致

## 2、numpy中数组运算方法
### 2.1 矩阵函数
|   方法                |       说明                                        |
|-----------------------|-----------------------------------------------------|
| np.dot() 、 np.matmul()|矩阵相乘
| np.transpose()        |矩阵装置
| np.linalg.inv()       |矩阵求逆，详见numpy.linalg函数介绍
| np.trace()            |计算对角线元素的和
| np.diag(ndarray)      |以一维数组的形式返回方阵的对角线（或非对角线）元素
| np.diag([x,y,...])    |将一维数组转化为方阵（非对角线元素为0）

### 2.2 numpy.linalg函数
|   方法                        |       说明                                        |
|-------------------------------|---------------------------------------------------|
|np.linalg.det(ndarray)	        |计算矩阵列式
|np.linalg.eig(ndarray)	        |计算方阵的本征值和本征向量
|np.linalg.inv(ndarray)         |计算方阵的逆
|np.linalg.pinv(ndarray)        |计算方阵的Moore-Penrose伪逆
|np.linalg.qr(ndarray)	        |计算qr分解 
|np.linalg.svd(ndarray)	        |计算奇异值分解svd
|np.linalg.solve(ndarray)	    |解线性方程组Ax = b，其中A为方阵 
|np.linalg.lstsq(ndarray)	    |计算Ax=b的最小二乘解 

### 2.3 数组元素的运算
|   方法                        |       说明                                        |
|-------------------------------|---------------------------------------------------|
|   np.sum()                    |求和
|   np.prod()                   |所有元素的乘积
|   np.diff()                   |计算数组相邻元素之间的差
|   np.sqrt()                   |计算各元素的平方根
|   np.square()                 |计算x^2
|   np.exp()                    |计算各元素的指数值
|   np.abs()                    |取各元素的绝对值：e^x
|   np.mean()                   |求平均值
|   np.modf(ndarray)            |将数组的小数和整数部分以两个独立的数组方式返回

### 2.4 数组堆叠运算
|   方法                        |       说明                                        |
|-------------------------------|---------------------------------------------------|
|  np.stack((数组1,数组2,...),axis)|axis决定堆叠的方向,axis=0,1,2,3...

## 3、numpy中随机数函数
### 3.1 numpy.random常用函数
|    函数                           |       说明                               | 返回值  |
|-----------------------------------|-----------------------------------------|--------|
|   np.random.seed()                |随机数种子                                     |
|   np.random.rand(d0,d1,..,dn)     |元素在[0,1)区间均匀分布的数组                  |浮点数
|   np.random.uniform(low,hige,size)|元素在[low,hige)区间均已分布                   |浮点数
|   np.random.randint(low,hige,size)|元素在[low,hige)区间均已分布                   |整数
|   np.random.randn(N, M, ...)      |生成一个N*M*...的标准正态分布（平均值为0，标准差为1）|浮点数
|   np.random.normal(loc,scale,size)|产生正太(高斯)分布数组，loc均值 scale方差         |浮点数

### 3.2 乱序函数
|   函数                      |       说明                                        |
|-------------------------------|---------------------------------------------------|
|   np.random.shuffle(序列)     |打乱序列元素顺序