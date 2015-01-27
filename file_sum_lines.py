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
__author__ = "ZhouKe"

f = file('score.txt','r')
lines = f.readlines()
f.close()

results = []

for line in lines:
    data = line.split()
    sumscore = 0
    for score in data[1:]:
        sumscore += int(score)
    result = '%s: \t %d\n' % (data[0], sumscore)
    results.append(result)

output = file('result.txt', 'w')
output.writelines(results)
output.close()

"""
score.txt
======================
name1 12 34 56 67 78
name2 45 56 67 90
name3 97 32 45 23

result.txt
======================
name1: 	 247
name2: 	 258
name3: 	 197
"""