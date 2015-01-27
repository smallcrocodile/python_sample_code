#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# Name:        []
# Purpose:
# Author:      [ZhouKe]
# Created:     201 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
#-------------------------------------------------------------------------------
import sys

reload(sys)
sys.setdefaultencoding('gbk')

mylist = ["苹果","梨","桔子"]

for fruit in mylist:
    print(fruit)

print join(mylist)
