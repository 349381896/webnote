
import jieba
import wordcloud
from scipy.misc  import  imread
mask = imread("python课堂笔记/static/china.png")
f = open("python课堂笔记/static/新时代中国特色社会主义.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="python课堂笔记/static/simsun.ttc",\
        width=1000,height=700,background_color="white",\
        mask=mask)
w.generate(txt)
w.to_file("python课堂笔记/static/txt2.png")