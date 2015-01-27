#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
# -------------------------------------------------------------------------------
# FileName:     []
# Purpose:      []
# Author:       [Zhou Ke]
# Created:      [2014--]
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------
"""
from Tkinter import *

root = Tk()


def callback(event):
    print "clicked at", event.x, event.y


frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()
root.mainloop()