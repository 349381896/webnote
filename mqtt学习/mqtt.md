
## 1、MQTT报文
|名称 	| 值 	| 流方向 	| 描述
|-------|-------|----------|---------------------------------------
|Reserved        （0000xxxx） 	|0 |	不可用 	       | 保留位
|CONNECT       （0001xxxx） 	|1 |	客户端到服务器 |	客户端请求连接到服务器
|CONNACK       （0010xxxx） 	|2 |	服务器到客户端 |	连接确认
|PUBLISH          （0011xxxx） 	|3 |	双向 	       |  发布消息
|PUBACK          （0100xxxx） 	|4 |	双向 	       |  发布确认
|PUBREC          （0101xxxx） 	|5 |	双向 	       |  发布收到（保证第1部分到达）
|PUBREL           （0110xxxx） 	|6 |	双赂 	       | 发布释放（保证第2部分到达）
|PUBCOMP        （0111xxxx） 	|7 |	双向 	       | 发布完成（保证第3部分到达）
|SUBSCRIBE     （1000xxxx） 	|8 |	客户端到服务器 | 	客户端请求订阅
|SUBACK          （1001xxxx） 	|9 |	服务器到客户端 |	    订阅确认
|UNSUBSCRIBE（1010xxxx） 	    |10| 	客户端到服务器 |	    请求取消订阅
|UNSUBACK      （1011xxxx） 	|11| 	服务器到客户端 |	    取消订阅确认
|PINGREQ         （1100xxxx） 	|12| 	客户端到服务器 |	    PING请求
|PINGRESP       （1101xxxx） 	|13| 	服务器到客户端 |	    PING应答
|DISCONNECT  （1110xxxx） 	    |14| 	客户端到服务器 |	    中断连接
|Reserved          （1111xxxx） |15| 	不可用 	       |     保留位
 