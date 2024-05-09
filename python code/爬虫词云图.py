# coding=gbk
# -*- coding:uft-8 -*-
# ΢�����ӻ�

from wordcloud import WordCloud
import jieba
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img = Image.open("D:\Ǯ.png")  # ������ͼƬ
mask = np.array(img)
df = pd.read_excel('D:\��ͨ�ƾ�-���-�����ı�.xlsx', engine='openpyxl')
stop = []
kinds = df['�����ı�'].tolist()
words = jieba.cut('/'.join(kinds))
newtxt = ''
stopwords = ["����","����","����","����","����","�Լ�","���","����","����","����","��","��","��","��","��","��","��","Ҳ","��","��","��","��","����","�ܶ�","û��"]
for word in words:
    if len(word) > 1 and word not in stop:
        newtxt += word + '/'
wordcloud = WordCloud(background_color='white', mask = mask,width=800, height=600, font_path='msyh.ttc', max_words=200,
                      max_font_size=130,stopwords=stopwords).generate(newtxt)
plt.imshow(wordcloud, interpolation='bilinear')  # ��plt��ʾͼƬ
plt.axis("off")  # ����ʾ������
plt.show()  # ��ʾͼƬ
wordcloud.to_file('D:\���1.png')
