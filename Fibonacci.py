#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# File Name:
# Author: Zhou Ke
# Creation Date: 2014-11- 
# Description: Fibonacci number serial
# Modification Date: 
# Changes:

def fib(n):
    """

    :rtype : print
    """
    a = 0
    b = 1
    for i in range(n):
        a, b = b, b + a
        print(i),
        print(b)

fib(50)