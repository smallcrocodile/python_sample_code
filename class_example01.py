#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:     multiple_replace
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
#-------------------------------------------------------------------------------


class M:
    def __init__(self, mx = None):
        self.mx = mx

    def show(self):
        print('M.mx', self.mx)
        return True


class N:
    def __init__(self, nx=None):
        self.nx = nx
        self.mnx = []


def f():
    m = M(3)
    n = N(2)
    print(m.mx)
    n.mnx.append(m)

    print(len(n.mnx))
    n.mnx[0].show()

    return

f()