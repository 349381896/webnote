from sklearn.datasets import load_boston
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
boston = load_boston()
regressor = DecisionTreeRegressor(random_state=0) #使用回归树
cross_val_score(regressor,          boston.data,        boston.target,  cv=10,          scoring = "neg_mean_squared_error")
#               创建好的模型          完整的数据源          完整的标签     10次交叉运算     评分模型=“负均方误差”  不填返回R^2  
#交叉验证cross_val_score的用法