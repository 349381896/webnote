# import matplotlib.pyplot as plt 
# plt.figure(figsize=(8,4),facecolor='w')
# plt.rcParams["font.sans-serif"]="SimHei"
# plt.rcParams["axes.unicode_minus"] = False
# plt.subplot(2,2,1)
# plt.title("子标题1")
# plt.text(0,0,"测试")
# plt.subplot(2,2,2)
# plt.title("子标题2")
# plt.subplot(2,2,3)
# plt.title("子标题3")
# plt.subplot(2,2,4)
# plt.title("子标题4")
# plt.suptitle("全局标题")
# #plt.subplots_adjust(wspace =0.2, hspace =0.4)#调整子图
# plt.tight_layout(rect=[0,0,1,0.9])

# plt.plot()
# plt.show()

# import matplotlib.pyplot as plt 
# import numpy as np
# plt.rcParams["font.sans-serif"]="SimHei"
# plt.rcParams["axes.unicode_minus"] = False

# n=1024
# x1 = np.random.normal(0,1,n)
# y1 = np.random.normal(0,1,n)

# x2 = np.random.uniform(-4,4,n)
# y2 = np.random.uniform(-4,4,n)
# plt.scatter(x1,y1,color='b',marker='*',label='正态分布')
# plt.scatter(x2,y2,color='y',marker='o',label='均与分布')
# plt.legend(loc=2)
# plt.title('标准正态分布',fontsize=20)
# plt.text(2.5,2.5,"均  值：0\n标准差：1")

# plt.xlim(-4,4)
# plt.ylim(-4,4)

# plt.xlabel('横坐标',fontsize=14)
# plt.ylabel('纵坐标',fontsize=14)
# plt.show()

import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams["font.sans-serif"]="SimHei"
plt.rcParams["axes.unicode_minus"] = False

n=24
y1 = np.random.randint(27,37,n)
y2 = np.random.randint(40,60,n)

plt.plot(y1,color='r',label='温度')
plt.plot(y2,color='g',label='湿度') 
plt.legend(loc=1)
plt.title('24小时温湿度统计',fontsize=20)
plt.xlim(0,23)
plt.ylim(20,70)


plt.xlabel('小时',fontsize=12)
plt.ylabel('测量值',fontsize=13)
plt.show()


