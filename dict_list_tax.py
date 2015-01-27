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
import  random
# generate name and salary for 50 staff
ds = { 'name' + str(i) : random.randint(1, 200000) for i in range(50)}
ll = [0,    3000,   6000,     10000,   20000,  50000, 100000]
lr = [0,    0.05,   0.1,      0.2,      0.3,    0.4,    0.45]

for (name, salary) in ds.items():
    print( )







