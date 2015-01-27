#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# -------------------------------------------------------------------------------
# FileName:     []
# Purpose:      []
# Author:       [Zhou Ke]
# Created:      [2014--]
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------
"""

import re
# 导入正则表达式模块为了识别关键字单词，过滤掉标点符号。
source_file = r'd:\a.txt'
result_file = r'd:\b.txt'
# 要合并关键字的文本文件的路径和文件名


with open(source_file, mode='r') as fs:

    while True:
        line = fs.readline().strip('\n').decode('utf-8')
        if not line:
            break
        key_value = re.split('\s\W+\s', line, 1)
        # '\w+' 正则表达式\w表匹配单词, +代表1或多个
        # words 是返回的一个list
        print(key_value[0])

