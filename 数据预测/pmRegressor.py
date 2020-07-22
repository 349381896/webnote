from sklearn.linear_model import LinearRegression as LR  #导入线性回归模型
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.datasets import fetch_california_housing as fch #加利福尼亚房屋价值数据集
import pandas as pd
import matplotlib.pyplot as plt



# housevalue = fch() #会需要下载，大家可以提前运行试试看
# X = pd.DataFrame(housevalue.data) #放入DataFrame中便于查看
# y = housevalue.target
# print(X.shape)
# print(y.shape)
# print(X.head())

data = pd.read_csv(r"E:\pycharm file\huaweidev\SELECT_t___FROM_pm2_5with_pm10_day_t.csv")  #导入csv数据文件
column = ['pm2','pm10','daytime']
# #筛选特征
# data.drop(["id","deviceid","pm10"],inplace=True,axis=1) #inplace覆盖，axis=1对列操作

print(data.shape)
