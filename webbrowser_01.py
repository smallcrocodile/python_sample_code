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
# coding=utf-8
import webbrowser as web
import time
import os
import random

M = random.randint(10, 15)
print '随机数  = ', M
N = 10
j = 0
while j < M:
    i = 0
    while i < N:
        web.open_new_tab('http://www.bjzba.com')
        i = i + 1
        time.sleep(15)
    else:
        os.system('taskkill /F /IM firefox.exe')
    j = j + 1
else:
    print '本次python总共打开了', M * N, '次'
# o = 'c:\\windows\\system32\\shutdown -s '
# os.system(o)