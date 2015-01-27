#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

numbers = []
while True:
    temp_line = raw_input('Please input numbers:')
    if temp_line:
        for num in temp_line.split():
            try:
                numbers.append(int(num))
            except ValueError:
                print('%s is not number!' % num)
    else:
        break
print(numbers)

