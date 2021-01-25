# Keras是一个高层的神经网络和深度学习库
>TensorFlow2.0将其加入了官方API，其内置了一些公共数据集可通过tf.keras.datasets模块加载和访问

**Keras中集成的数据集**                
1.          .boston_housing          波士顿房价数据
2.          .CIFAR10                 十种类别的图片集
3.          .CIFAR100                100种类别的图片集
4.          .MNIST                   手写数字图片集
5.          .Fashion-MNIST           10种时尚类别的图片集
6.          .IMDB                    电影点评数据
7.          .reuters                 路透社新闻数据

>有些数据集并没有在tensorflow中集成，但可以通过get_file()函数下载数据集

**tf.keras.utils.get_file(fname,origin,cache_dir)**
|   参数        |           说明                            |
|---------------|-------------------------------------------|
|   fname       |   下载后的文件名  
|   origin      |   文件的URL地址
|   cache       |   下载后的存储位置，默认：C:\User\\Administrator\.keras\datasets
-返回值：下载后的文件在本地磁盘的绝对路径