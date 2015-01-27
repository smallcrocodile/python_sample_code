#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:     String handling realized on Python 2.7.8
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
#-------------------------------------------------------------------------------

# Way 1, using pure string method
t = raw_input('Please input your full name: ')
uid = t[t.rindex(' '):t.rindex(' ') + 5].upper() + t[0].upper() + \
      t[t.index(' ')+1].upper() + str(len(t[t.rindex(' '):]))
print(uid)

# Way 2, using list method
fullname = raw_input('Please input your full name: ')
nl = fullname.split(' ')
uid = nl[2][0:4].upper() + nl[0][0].upper() + nl[1][0].upper() + str(len(nl[2]))
print(uid)


