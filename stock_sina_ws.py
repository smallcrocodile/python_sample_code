#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import string

mystock = [ ['000963',500,23.854],
            ['002001',300,34.581],
            ['002003',500,23.694],
            ['002204',500,21.953],
                 ]

url  = "http://hq.sinajs.cn/list=\
s_sh000001,\
s_sz399001,\
s_sz002003,\
s_sz002001,\
s_sz000963,\
s_sz002204,\
s_sz000839,\
s_sz002194,\
s_sh600893,\
s_sh600839,\
s_sh600418,\
s_sh600104"

def name_in_mystock (name):
          i = 0
          for s in mystock:
                  i = i + 1
                  if name.find (s[0]) is not -1:
                          return i
          return 0


data = urllib.urlopen(url).read()

line = data.split('\n')
for vv in line:
  aa = vv.split(',');
  if aa[0] :
          name  = aa[0].split('_')[3].replace('"','').replace('=','   ')
          cur   = string.atof(aa[1])
          wave  = string.atof(aa[2])
          per   = string.atof(aa[3])
          money = string.atof(aa[5].replace('";',''))

          index = name_in_mystock (name)
          if index :
                  mypri = mystock[index-1][2]
                  mypro = (cur - mypri) * mystock[index-1][1];
                  print '%s %10.2f %10.2f %10.2f %12d w %10.3f %10.2f' %(name, cur, wave, per, money, mypri, mypro)
          else:
                  print '%s %10.2f %10.2f %10.2f %12d w' %(name, cur, wave, per, money)