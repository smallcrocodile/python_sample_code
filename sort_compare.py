#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import random

l = [random.randint(1,100) for i in range(20)]

print(l)

def bubbleSort(data):
    if len(data) < 2: return data
    for i in range(0, len(data)-1):
        m = i
        for j in range(i+1, len(data)):
            if data[m] > data[j]: m =j

        if m != i:
            data[i], data[m] = data[m], data[i]
    return data


def insertSort(data):
    if len(data) < 2: return data
    for i in range(1,len(data)):
        print data
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j = j-1
        data[j+1]= key
    return data


l1 = l[:]
bubbleSort(l1)

l2 = l[:]
insertSort(l2)

print(l1)

print(l2)