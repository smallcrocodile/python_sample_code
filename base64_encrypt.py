#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# Name:        []
# Purpose:
# Author:      [ZhouKe]
# Created:     201 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------

import base64

a = "Hello world!"
b = base64.encodestring(a)  #加密
c = base64.decodestring(b)  #解密

print(a)
print(b)
print a == c