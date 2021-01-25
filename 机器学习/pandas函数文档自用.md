# pandas库一些常用函数、方法记录（自用，其中有很多是参考官方和网友的，这里只是简单汇总）
```import pandas as pd```

## 1）、pd.Series(data, index=index, dtype=dtype)
|    参数           |                   说明                        |
|-------------------|-----------------------------------------------|
|   data            |数据，可以是列表，字典或Numpy数组
|   index           |索引，为可选参数
|   dtype           |数据类型，为可选参数

##  2)、df = pd.DataFrame(data, index=index, columns=columns) DataFrame对象的创建
- 当axis=1时，数组的变化是横向的，体现出列的增加或者减少。反之，当axis=0时，数组的变化是纵向的，体现出行的增加或减少。

|    参数           |                   说明                        |
|-------------------|-----------------------------------------------|
|   data            |数据，可以是列表，字典或Numpy数组
|   index           |索引，为可选参数
|   columns         |列标签，为可选参数

### 2-1）、DataFrame对象性质(二维表格)
|    属性           |                   说明                        |
|-------------------|-----------------------------------------------|
|   df.values       |返回numpy数组表示的数据
|   df.index        |返回行索引
|   df.columns      |返回列索引
|   df.shape        |返回形状
|   df.size         |返回大小
|   df.dtypes       |返回每列数据类型
|   df.T            |装置
|   df.nidm         |维数

### 2-2）、对DataFrame对象数据方法
|   方法            |                   说明                        |
|-------------------|-----------------------------------------------|
|   df.head(n)       |查看 DataFrame 数据中头部
|   df.tail(3)      |查看 DataFrame 数据中尾部
|   df.describe()   |查看对于数据的快速统计汇总。最大值、最小值等
|   df.sort_index(axis=1, ascending=False)|按轴进行排序,False降序
|   df.sort_values(by='B')|按值进行排序,已被改使用values
|   df.as_matrix()  |将Dataframe的表格型数据转换成数组
|   df.loc()        |根据index标签（xy轴都可）来索引
|   df.iloc(:,1:3)  |根据行号来索引，行号从0开始，逐次加1
|   df[df.A > 0],df[df > 0]|选择数据
|   df2[df2['E'].isin(['two','four'])]|.isin()过滤
|   df.at[dates[0],'A'] |根据标签设置新的值
|   df.iat[1,o]     |通过位置设置新的值
|   df.reindex()    |对指定轴上的索引进行改变/增加/删除操作， 这将返回原始数据的一个拷贝
|   df.dropna(how='any')|去掉包含缺失值的行
|   df.fillna(value=5) |对缺失值进行填充
|   pd.isnull(df)       |对数据进行布尔填充


## 3）、连接函数：pd.concat(
    objs, axis=0, join='outer', join_axes=None, ignore_index=False,keys=None, levels=None, names=None, verify_integrity=False,copy=True)**

|    参数           |                   说明                        |
|-------------------|-----------------------------------------------|
|       objs               |Series，DataFrame或Panel对象的序列或映射。如果传递了dict，则排序的键将用作键参数，除非它被传递，在这种情况下，将选择值。任何无对象将被静默删除，除非它们都是无，在这种情况下将引发一个ValueError。
|       axis               |{0,1，...}，默认为0。沿着连接的轴即按行操作。
|       join               |{'inner'，'outer'}，默认为“outer”。如何处理其他轴上的索引。outer为联合和inner为交集。
|       ignore_index       |boolean，default为False。如果为True，请不要使用并置轴上的索引值。结果轴将被标记为0，...，n-1。如果要连接其中并置轴没有有意义的索引信息的对象，这将非常有用。注意，其他轴上的索引值在连接中仍然受到尊重。
|       join_axes          |Index对象列表。用于其他n-1轴的特定索引，而不是执行内部/外部设置逻辑。
|       keys               |序列，默认值无。使用传递的键作为最外层构建层次索引。如果为多索引，应该使用元组。
|       levels             |序列列表，默认值无。用于构建MultiIndex的特定级别（唯一值）。否则，它们将从键推断。
|       names               |list，default无。结果层次索引中的级别的名称。
|       verify_integrity    |boolean，default False。检查新连接的轴是否包含重复项。这相对于实际的数据串联可能是非常昂贵的。
|       copy                |boolean，default True。如果为False，请勿不必要地复制数据。

## 4）、对数据应用函数apply() 函数##
```
In [66]: df.apply(np.cumsum)
Out[66]:
A B C D F
2013-01-01 0.000000 0.000000 -1.509059 5 NaN
2013-01-02 1.212112 -0.173215 -1.389850 10 1.0
2013-01-03 0.350263 -2.277784 -1.884779 15 3.0
2013-01-04 1.071818 -2.984555 -2.924354 20 6.0
2013-01-05 0.646846 -2.417535 -2.648122 25 10.0
2013-01-06 -0.026844 -2.303886 -4.126549 30 15.0

In [67]: df.apply(lambda x: x.max() - x.min())
Out[67]:
A 2.073961
B 2.671590
C 1.785291
D 0.000000
F 4.000000
dtype: float64
```

## 5）、pandas的一些统计函数
|       方法            |   说明
|-----------------------|----------------------------------------------------------
|       count	        |非 NA 值的数量
|       describe    	|针对 Series 或 DF 的列计算汇总统计
|       min , max	    |最小值和最大值
|       argmin , argmax	|最小值和最大值的索引位置（整数）
|       idxmin , idxmax	|最小值和最大值的索引值
|       quantile	    |样本分位数（0 到 1）
|       sum	            |求和
|       mean	        |均值
|       median	        |中位数
|       mad	            |根据均值计算平均绝对离差
|       var	            |方差
|       std	            |标准差
|       skew	        |样本值的偏度（三阶矩）
|       kurt	        |样本值的峰度（四阶矩）
|       cumsum	        |样本值的累计和
|       cummin , cummax	|样本值的累计最大值和累计最小值
|       cumprod	        |样本值的累计积
|       diff	        |计算一阶差分（对时间序列很有用）
|       pct_change	    |计算百分数变化
|       prod	        |不同维度上的乘积


## 6)、Pandas读取csv数据集
**pd.resd_csv(filepath_or_buffer,header,names,nrows,skiprows)**
|       参数             |   说明
|-----------------------|----------------------------------------------------------
|   filepath_or_buffer |文件所在处的路径
|   header              |指定哪一行作为表头。默认设置为0（即第一行作为表头），如果没有表头的话，要修改参数，设置header=None
|   names               |指定列的名称，用列表表示。一般我们没有表头，即header=None时，这个用来添加列名就很有用啦！
|   nrows               |需要读取的行数
|   skiprows            |需要跳过的行号列表（从0开始)
|   encoding            |乱码的时候用这个就是了