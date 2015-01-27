#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymssql

conn = pymssql.connect(host='192.168.1.114', port='1433', user='sa', \
                       password='Agtech123', database='test', as_dict=True)
cur = conn.cursor()

cur.execute('SELECT * FROM namelist WHERE id=%s', '002')
for row in cur:
    print "ID=%d, Name=%s" % (row['id'], row['name'])

conn.close()