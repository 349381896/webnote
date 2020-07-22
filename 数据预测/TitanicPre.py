#1. 导入所需要的库
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

data = pd.read_csv(r"CommonData\data.csv")  #导入csv数据文件
data.info()#常看综合信息
data.head()#查看头部数据

#筛选特征
data.drop(["Cabin","Name","Ticket"],inplace=True,axis=1) #inplace覆盖，axis=1对列操作

#处理缺失值
data["Age"] = data['Age'].fillna(data["Age"].mean())#用均值填补缺失值
data = data.dropna(axis=0) #删除有缺失值的行

#将三分类变量转换为数值型变量
labels = data["Embarked"].unique().tolist()    #去除非重复值 并转化为列表
data["Embarked"] = data["Embarked"].apply(lambda x: labels.index(x)) #用下标取代字符

#将二分类变量转换为数值型变量
#astype能够将一个pandas对象转换为某种类型，和apply(int(x))不同，astype可以将文本类转换为数字，用这
#个方式可以很便捷地将二分类特征转换为0~1
data.loc[:,"Sex"] = (data["Sex"]== "male").astype("int") #astype将布尔值转化为数值
#       行，列-但只能是表头


x = data.iloc[:,data.columns != "Survived"]  #提取特征值

y = data.iloc[:,data.columns == "Survived"]  #提取标签 
  
Xtrain,Xtest,Ytrain,Ytest = train_test_split(x,y,test_size=0.3)  #37分，xtrain为70%
#修正测试集和训练集的索引
for i in [Xtrain, Xtest, Ytrain, Ytest]:
    i.index = range(i.shape[0])

clf = DecisionTreeClassifier(random_state=25) #分类树
clf = clf.fit(Xtrain, Ytrain)
score_ = clf.score(Xtest, Ytest)

score = cross_val_score(clf,x,y,cv=10).mean() #交叉验证

tr = []
te = []
for i in range(10):
    clf = DecisionTreeClassifier(random_state=25
        ,max_depth=i+1
        ,criterion="entropy"
        )
    clf = clf.fit(Xtrain, Ytrain)
    score_tr = clf.score(Xtrain,Ytrain) 
    score_te = cross_val_score(clf,x,y,cv=10).mean()
    tr.append(score_tr)
    te.append(score_te)
print(max(te)) #最大均值
plt.plot(range(1,11),tr,color="red",label="train")
plt.plot(range(1,11),te,color="blue",label="test")
plt.xticks(range(1,11))
plt.legend()
plt.show()
#这里为什么使用“entropy”？因为我们注意到，在最大深度=3的时候，模型拟合不足，在训练集和测试集上的表现接
#近，但却都不是非常理想，只能够达到83%左右，所以我们要使用entropy。


#网格搜索：帮助我们同时调整多个参数的技术，枚举技术，计算量大
#parameters是一串参数和这些参数对应的，我们希望网格搜索来搜索的参数的取值范围
import numpy as np
gini_thresholds = np.linspace(0,0.5,20) #0-0.5有顺序的列表  基尼系数
parameters = {'splitter':('best','random')
    ,'criterion':("gini","entropy")
    ,"max_depth":[*range(1,10)]
    ,'min_samples_leaf':[*range(1,50,5)]
    ,'min_impurity_decrease':[*np.linspace(0,0.5,20)]
    }
clf = DecisionTreeClassifier(random_state=25)
GS = GridSearchCV(clf,parameters,cv)
GS = GS.fit(Xtrain,Ytrain)
