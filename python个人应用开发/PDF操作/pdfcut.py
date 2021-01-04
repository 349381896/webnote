from PyPDF2 import PdfFileWriter, PdfFileReader

# 开始页
start_page = 192

# 截止页
end_page = 261

output = PdfFileWriter()
pdf_file = PdfFileReader(open("F:\考研资料/2021腿姐政治冲刺背诵手册【微信公众号】免费分享.pdf","rb"))
pdf_pages_len = pdf_file.getNumPages()

# 保存input.pdf中的1-5页到output.pdf
for i in range(start_page, end_page):
    if((i+1)%5):
        output.addPage(pdf_file.getPage(i))

outputStream = open("F:\考研资料/剪切后的背诵手册.pdf", "wb")
output.write(outputStream)