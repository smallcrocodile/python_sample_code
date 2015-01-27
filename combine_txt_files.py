#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
#-------------------------------------------------------------------------------


# -*- coding: utf-8 -*-
# 功能：合并多个文本文件到一个文件中
import os
fpath = r'd:\media\buffer'  # 要合并的文件目录或os.getcwd()取当前目录
fout = open(r'd:\media\combined.txt', 'w')  # 合并内容到该文件

def writeintofile(f_filename):
    fin = open(f_filename)
    strinfo = fin.read()
    # 利用##作为标签的点缀，你也可以使用其它的
    fout.write('\n##\n')
    fout.write('## '+f_filename[-30:].encode('utf-8'))
    fout.write('\n##\n\n')
    fout.write(strinfo)
    fin.close()

for filename in os.listdir(fpath):
    fullpath = "%s\%s" % (fpath,filename)
    if fullpath[-3:] == 'txt': # 只将后缀名为txt的文件内容合并
        writeintofile(fullpath)

fout.close()
