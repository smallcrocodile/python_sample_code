#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------

import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table a(i)")
for i in range(500):
    cur.execute("insert into a(i) values (%s)" % i)
cur.execute("select i from a")

for j in range(500):
    res = cur.fetchone()[0]
    print(res)
cur.close()
con.close()
