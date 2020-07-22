#1. 导入需要的库
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

#2. 创建一条含有噪声的正弦曲线
rng = np.random.RandomState(1)  #随机数种子
X = np.sort(5 * rng.rand(80,1), axis=0) #80行1列随机数 0-5  sort排序-方向为axis=0
y = np.sin(X).ravel()       #生产正弦值 再用recal()降为一维
y[::5] += 3 * (0.5 - rng.rand(16)) #以5为步长切片生成列表 + 16个随机数（-1.5 ~ 1.5）

#np.random.rand(数组结构)，生成随机数组的函数
#了解降维函数ravel()的用法
np.random.random((2,1))
np.random.random((2,1)).ravel()
np.random.random((2,1)).ravel().shape  #shape返回（行，列）值

#3. 实例化&训练模型
regr_1 = DecisionTreeRegressor(max_depth=2)  #max_depth是树的最大深度，设置高决策树学习太精细，
#                                           它从训练数据中学习了很多细节，包括噪声得呈现，从而使模型偏离真实的正弦曲线
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)

#4. 测试集导入模型，预测结果
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis] #生成二维数组
#np.arrange(开始点，结束点，步长) 生成有序数组的函数
y_1 = regr_1.predict(X_test)  #
y_2 = regr_2.predict(X_test)

#了解增维切片np.newaxis的用法
l = np.array([1,2,3,4])
l
l.shape
l[:,np.newaxis]
l[:,np.newaxis].shape #增加行
l[np.newaxis,:].shape #增加列

#5. 绘制图像
plt.figure()  #绘布
plt.scatter(X, y, s=20, edgecolor="black",c="darkorange", label="data") #散点图 
plt.plot(X_test, y_1, color="cornflowerblue",label="max_depth=2", linewidth=2) #绘制折线
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")  #x
plt.ylabel("target") #y
plt.title("Decision Tree Regression") #标题
plt.legend() #显示图列
plt.show()#绘制