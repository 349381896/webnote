import  xlrd	#pip install xlrd
import  xlwt	#pip install xlwt

data  =  xlrd.open_workbook('附表：稀土专利数据.xls')
workbook = xlwt.Workbook(encoding = 'utf-8')#创建一个表

table = data.sheet_by_name('数据表1')#通过名称获取对象
print(table.nrows) #行
print(table.ncols) #列

nameid = ["授权","非授权"]
		
worksheet=[]
#===========添加sheet，并添加每一个sheet的首行======
for x in range(0,2):	
	work = workbook.add_sheet(nameid[x])
	worksheet.append(work)
	for y in range(0,table.ncols):
		worksheet[x].write(0,y,table.row_values(0)[y])
count=[]		

#添加授权数据
for i in range(0,2):
	count.append(i)
	count[i] =1
	for rowx in range(1,table.nrows):
		row =table.row_values(rowx)    #行
		if(row[2] == nameid[i]):
			for y in range(0,table.ncols):
				worksheet[i].write(count[i],y,row[y])
			count[i] = count[i] +1

#单独添加其余数据
count = 1
for rowx in range(1,table.nrows):
	row =table.row_values(rowx)    #行
	if row[2]  in nameid:	
		{}
	else:	
		for y in range(0,table.ncols):
			worksheet[-1].write(count,y,row[y])
		count = count +1
workbook.save("授权专利.xls")
