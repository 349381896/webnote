#PDF合并
from PyPDF2 import PdfFileMerger,PdfFileReader
import  os
basicpath = os.getcwd()+'merge.pdf'
def pdfmerge(PathTable,OutPath):
    merger = PdfFileMerger()    #创建一个合并对象
    if OutPath=='':
        OutPath = basicpath
    pdfmergepath=[]
    for pdfpath in PathTable:
        if pdfpath =='':
            break
        pdf = pdfpath.replace('\\', '/')
        pdfmergepath.append(pdf)
    for i in range(len(pdfmergepath)):  
        print( pdfmergepath[i])
        merger.merge(0,fileobj = pdfmergepath[i])     
    with open(OutPath,'wb') as file:
        merger.write(file)
    
    return 1

if __name__ == "__main__":
    pdfmerge(['C:\\Users/day_day_up/Desktop/zdh172_2420172894(14)_肖春明.pdf','F:\\b.pdf','','',''],'F:\c.pdf')