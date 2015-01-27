#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:     multiple_replace
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------


d = {}
with open('source.txt', 'r') as fr:
    lines = fr.readlines()
    for line in lines:
        ll = line.split(',')
        key = ll[0] + ',' + ll[1]
        value = ll[-1].strip('\n')
        if key in d:
            value = d[key] + ',' + value
        d[key] = value

with open('result.txt', 'w') as fw:
    for k, v in d.items():
        fw.write(k + ',' + v + '\r\n')
        # Windows OS string end using '\r\n', Linux usring '\n'

# ===============================================================
"""
source.txt

a，b，1
a，b，2
a，b，1
a，c，1
a，c，2
b，c，2

result.txt
a,b,1,2,1
a,c,1,2
b,c,2

"""

