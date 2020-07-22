#PDF合并
from PyPDF2 import PdfFileMerger,PdfFileReader
merger = PdfFileMerger()
input1 = open("C:/Users/day_day_up/Desktop/软件著作权/软件技术特点概要设计说明书.pdf","rb")
input2 = open("C:/Users/day_day_up/Desktop/软件著作权/软件著作权设计说明书范本.pdf","rb")
merger.append(fileobj = input1)
merger.merge(position = 2,fileobj = input2)
output = open("sumpdf.pdf","wb")
merger.write(output)