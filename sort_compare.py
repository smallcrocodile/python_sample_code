#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import random

l = [random.randint(1,100) for i in range(20)]

print(l)

def bubbleSort(data):

    if len(data) < 2: return data
    for i in range(0, len(data)-1):
        # print data
        m = i
        for j in range(i+1, len(data)):
            if data[m] > data[j]: m =j

        if m != i:
            data[i], data[m] = data[m], data[i]
    return data


def insertSort(data):
    if len(data) < 2: return data
    for i in range(1,len(data)):
        # print data
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j = j-1
        data[j+1]= key
    return data


def rsort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    return rsort([lt for lt in sort_list[1:] if lt < sort_list[0]]) + sort_list[0:1] + rsort([ge for ge in sort_list[1:] if ge >= sort_list[0]])

l1 = l[:]
bubbleSort(l1)

l2 = l[:]
insertSort(l2)

l3 = l[:]
rsort(l)

print(l1)
print(l2)
print(l)