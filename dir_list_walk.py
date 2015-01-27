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

import os
from os.path import walk

def visit(arg, dirname, filenames):
    for filepath in filenames:
        print(os.path.join(dirname, filepath))

if __name__ == '__main__':
    root = 'd:\\patha'
    walk(root, visit, 0)

