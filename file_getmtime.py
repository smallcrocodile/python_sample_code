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

import datetime, os
t = os.path.getmtime('d:/')
tt = datetime.datetime.fromtimestamp(t)
ttt = tt.strftime('%Y') # 这是个时间格式化字符串，只能返回年份。更多使用方法参见手册。
print ttt

