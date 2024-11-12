#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2021/10/22 16:06
# @Author       : yhr
# @File         : WordCloud.py
# @Software     : PyCharm


# 导入扩展库
import re  # 正则表达式库
import jieba  # 结巴分词
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # 图像展示库
from imageio import imread

# 读取文件
fn = open('聊天记录.txt', encoding="utf-8")  # 打开文件
string_data = fn.read()  # 读出整个文件
fn.close()  # 关闭文件
# 文本预处理
rule = re.compile(u"[^a-zA-Z\u4e00-\u9fa5]")
string_data = rule.sub('', string_data)

# 文本分词
seg_list_exact = jieba.cut(string_data)  # 精简模式

object_list = list()
remove_words = ["没", " ", "嗯", "了", "是", "的", '我', '的', "在", "不", "就", "也", "你", "吧", "和", "啊"]
f = open('result', 'w', encoding='utf-8')
for word in seg_list_exact:  # 循环读出每个分词
    if word not in remove_words:  # 如果不在去除词库中
        f.write(''.join(word))  # 将过滤后的弹幕内容写入创建的[cl.txt]文件中

# 词频统计

f1 = open('result', 'r', encoding='utf-8')
data = f1.read()

'''
--将弹幕内容分割成词组，并组合成五角星的图案
'''
result = " ".join(jieba.lcut(data))
# 词频展示
color_mask = imread('heart.png')
wc = WordCloud(
    width=600,
    height=700,
    scale=9,
    background_color="lightpink",
    # background_color="white",
    # font_path='C:/Windows/Fonts/simhei.ttf',
    font_path='C:/Windows/Fonts/msyh.ttc',  # 设置字体格式
    mask=color_mask,  # 设置背景图
    max_words=300,  # 最多显示词数
    max_font_size=50  # 字体最大值
)
wc.generate(result)
wc.to_file("导出图片.png")  # 生成文件
plt.imshow(wc)  # 显示词云
plt.axis('off')  # 关闭坐标轴
plt.show()  # 显示图像
# pip3 install  imageio -i https://pypi.tuna.tsinghua.edu.cn/simple/
