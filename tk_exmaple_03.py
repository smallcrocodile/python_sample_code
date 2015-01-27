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
import time

root = Tk()
root.minsize(600, 480)
a = root.winfo_screenheight()
b = root.winfo_screenwidth()
cv = Canvas(root, width=a, height=b, bg='white')
rt = cv.create_text(200, 200, text='+', fill='red', font=("Fixdsys", 36, "bold"))
cv.pack()
root.after(2000, lambda: cv.itemconfig(rt, text='start'))
rtags = []
for i in range(10):
    cv.create_rectangle(300, 100 + i * 30, 500, 130 + i * 30, outline='blue', fill='white', tags='r' + str(i+1))
    rtags.append('r' + str(i + 1))

# main()

for num in range(10):
    cv.itemconfig(cv.find_withtag(rtags[num]), fill='red')
    root.update()
    time.sleep(1)

root.after(4900, lambda: cv.itemconfig(rt, text='stop'))
#root.after(5000, lambda:root.destroy())
root.mainloop()