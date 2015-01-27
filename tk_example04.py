#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox

class Applicatoin(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hellolabel = Tkinter.Label(self, text='Hello World!')
        self.hellolabel.pack()
        self.inputName = Tkinter.Entry(self)
        self.inputName.pack()
        self.alertButton = Tkinter.Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.inputName.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hellow %s' % name)

App = Applicatoin()
App.master.Title = 'Hello World!'
App.after()
App.mainloop()


