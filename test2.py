#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Queue import Queue

import random

import threading

import time

from Tkinter import *

global d


class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue

    def run(self):
        #global d
        d=random.randrange(8)
        print d
        a=d+1
        #time.sleep(0.3)
        self.data.put(d)


class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue

    def run(self):
        val=self.data.get()
        global dataset
        dataset=val
        #time.sleep(0.3)
        print dataset


def main():
    queue = Queue()
    producer = Producer('Pro.', queue)
    consumer = Consumer('Con.', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print 'All threads terminate!'


def caijidiaoyong():
    if __name__ == '__main__':
      main()
    cv.itemconfig(cv.find_withtag(rtags[dataset]), fill='red')

    cv.after(1,caijidiaoyong) #取成1会显示红色的方格，取成0就不显示


def fangge():
    global rtags
    rtags = []
    for i in range(10):
        cv.create_rectangle(700, 500 + i * 30, 900, 530 + i * 30, outline='blue', fill='white', tags='r' + str(i+1))
        rtags.append('r' + str(i + 1))


root = Tk()
a = root.winfo_screenheight()
b = root.winfo_screenwidth()
cv = Canvas(root, width=a, height=b, bg='white')
rt = cv.create_text(a / 2, b / 2, text='+', fill='red', font=("Fixdsys", 36, "bold"))
cv.pack()


root.after(2000, lambda:cv.itemconfig(rt,text='start'))

root.after(2000,lambda:fangge())

root.after(2000,lambda:caijidiaoyong())
print a

root.after(5000, lambda:cv.itemconfig(rt,text='stop'))
root.after(50000, lambda:root.destroy())
for loop in range(5):
    time.sleep(5)
    root.update()
root.mainloop()
