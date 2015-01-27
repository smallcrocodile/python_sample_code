#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------

# -*- coding: cp936 -*-
import Tkinter
import urllib


class Window:
    def __init__(self, root):
        self.root = root
        self.entryUrl = Tkinter.Entry(root)
        self.entryUrl.place(x=5, y=15)
        self.get = Tkinter.Button(root, text='download', command=self.Get)
        self.get.place(x=120, y=15)
        self.edit = Tkinter.Text(root)
        self.edit.place(y=50)
        self.edit.insert(Tkinter.END, "Please enter url with http:// header.")

    def Get(self):
        url = self.entryUrl.get()
        page = urllib.urlopen(url)
        data = page.read()
        # data = rdata.decode('GBK')
        self.edit.insert(Tkinter.END, data)
        page.close()


root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()