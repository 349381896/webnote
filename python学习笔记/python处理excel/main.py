import  xlrd	#pip install xlrd
import  xlwt	#pip install xlwt

data  =  xlrd.open_workbook('附表：稀土专利数据.xls')
workbook = xlwt.Workbook(encoding = 'utf-8')#创建一个表

table = data.sheet_by_name('数据表1')#通过名称获取对象
print(table.nrows) #行
print(table.ncols) #列

nameid = ["北京;11","天津;12","河北;13","山西;14","内蒙古;15","辽宁;21","吉林;22","黑龙江;23","上海;31",\
		  "江苏;32","浙江;33","安徽;34","福建;35","江西;36"  ,"山东;37","河南;41","湖北;42"  ,"湖南;43",\
		  "广东;44","广西;45","四川;51","贵州;52","云南;53"  ,"西藏;54","陕西;61","甘肃;62"  ,"青海;63",\
		  "宁夏;64","新疆;65","海南;66","中国台湾;71","广州;81","武汉;83","重庆;85","西安;87","沈阳;89",\
		  "大连;91","哈尔滨;93","深圳;94","青岛;95","宁波;97","中国香港;81","国外"]
worksheet=[]
#===========添加sheet，并添加每一个sheet的首行======
for x in range(0,43):	
	work = workbook.add_sheet(nameid[x])
	worksheet.append(work)
	for y in range(0,table.ncols):
		worksheet[x].write(0,y,table.row_values(0)[y])
		
count=[]

#添加国内主体数据
for i in range(0,43):
	count.append(i)
	count[i] =1
	for rowx in range(1,table.nrows):
		row =table.row_values(rowx)    #行
		if(row[3] == nameid[i]):
			for y in range(0,table.ncols):
				worksheet[i].write(count[i],y,row[y])
			count[i] = count[i] +1

#单独添加国外数据
count = 1
for rowx in range(1,table.nrows):
	row =table.row_values(rowx)    #行
	if row[3]  in nameid:	
		{}
	else:	
		for y in range(0,table.ncols):
			worksheet[-1].write(count,y,row[y])
		count = count +1
workbook.save("数据整合.xls")