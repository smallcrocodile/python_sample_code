#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

a = [1, 2, 4, 5, 6,7,8,9]

b = map(lambda x: 5 if x > 5 else x, a)
print(b)

f = lambda x: map((lambda y:y**2),x)
print(f([2,3,5]))
