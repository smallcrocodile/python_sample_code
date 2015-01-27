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


from Tkinter import *
root = Tk()

def draw_rect(n):
    cv = Canvas(root, bg='white')

    for i in range(10):
        if i <=n:
            color = 'white'
        else:
            color = 'red'
        sel = cv.create_rectangle(10, 10 + i*10, 50, 20 + i*10, outline='blue', fill=color)
    cv.pack()

draw_rect(3)

root.mainloop()