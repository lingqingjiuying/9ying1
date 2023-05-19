# 导入所需的库
import jieba
import docx
from docx import Document
from docx.shared import Inches
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


# 读取文档内容
filter_words = ['', '','','','','','','']
document = Document('221.docx')
text = ''
text= jieba.cut(text)
text = ''.join(str(x) for x in text)
for paragraph in document.paragraphs:
    text += paragraph.text + ' '
for word in filter_words:
    text = text.replace(word, '')

# 创建停用词集合
stopwords = set(STOPWORDS)
stopwords = ['同志们', '二','三','四','五','一','六','七','八','九','十','']
# 创建词云对象，并设置参数
wordcloud = WordCloud(
    font_path="simhei.ttf",
    width=1200, height=800,
    background_color='white',
    stopwords=stopwords,
    min_font_size=10).generate(text)

# 绘制词云图
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
# 创建需要过滤的词汇列表


# 加载需要过滤的文本
text = 'I hate this bad movie, it is so ugly and boring.'

# 使用字符串函数 replace() 进行替换


print(text)
