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


def pr(s):
    return s

x = 3
# functional method to realize if elif flow control
# logic result and function()
print (x == 1 and pr("one")) or (x == 2 and pr("two")) or (x == 3 and pr("three"))

lst = [1, 2, 3, 4, 5, 6, 7]

# using lambda function (without name) and map/filter/reduce handle iterable object
print(map(lambda n: n * 2, lst))

print(filter(lambda n: n % 2 == 0, lst))

print(reduce(lambda n, m: m * n, lst ))

for n in range(255):
    print(chr(n)),
lst


