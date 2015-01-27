#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
本程序可以统计一个英文文本文件中单词出现频率.
"""

from collections import Counter
# 从collections模块导入计数器类
import re
# 导入正则表达式模块为了识别单词，过滤掉标点符号。
filename = r'd:\words.txt'
# 要统计单词频率的文本文件的路径和文件名
wc = Counter()

with open(filename, mode='r') as fwords:

    while True:
        line = fwords.readline()
        if not line:
            break
        words = re.findall('\w+', line.lower())
        # '\w+' 正则表达式\w表匹配单词, +代表1或多个
        # words 是返回的一个list

        for word in words:
            wc[word] = wc[word] + 1


d = {word:number for (word, number) in wc.most_common(50)}

for w in sorted(d.iteritems(), key=lambda d:d[1], reverse=False):
    # 打印按出现次数排序
     print w[0], ':', '\t'*5, w[1]



