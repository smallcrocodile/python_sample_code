# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 20:36:34 2014

@author: duane
"""
from Queue import Queue  
  
import random  
  
import threading  
  
import time  
from Tkinter import *  
#global numbers  
#numbers=0  
#Producer thread  
def fenlei(num=0):
    
   
    cv.itemconfig(cv.find_withtag(rtags[num]), fill='red')
    
   
    cv.after(300,fenlei,num)#500不是次数
    cv.after(5000,lambda:root.destroy())
    del num
    #cv.after(5000,lambda:cv.destroy())#删除cv，但是tk界面还在
class Producer(threading.Thread):  
  
    def __init__(self, t_name, queue):  
      
        threading.Thread.__init__(self, name=t_name)  
      
        self.data=queue  
      
    def run(self):  
      
        d=random.randrange(8)
        print d
        #b=b-1
        self.data.put(d)
   
  
#Consumer thread  
  
class Consumer(threading.Thread):  
  
    def __init__(self, t_name, queue):  
      
        threading.Thread.__init__(self, name=t_name)  
      
        self.data=queue  
      
    def run(self):
        val=self.data.get()
        print val
        
        global numbers
        numbers=0
        numbers=val+1
        
        print numbers
        #self.data.put(c)
  
#Main thread  
  
def main():
    for i in range(10):
        
 
        queue = Queue()  
          
        producer = Producer('Pro.', queue)  
          
        consumer = Consumer('Con.', queue) 
        
          
        producer.start()  
          
        consumer.start()  
        
          
        producer.join()  
          
        consumer.join()
        print 'All threads terminate!'  
if __name__ == '__main__':
    main()
root = Tk()
a=root.winfo_screenheight()
b=root.winfo_screenwidth()
   
cv=Canvas(root,width=a,height=b,bg='white')
rt=cv.create_text(512,640,text='+',fill='red',font=("Fixdsys",36,"bold"))
cv.pack()
root.after(2000, lambda:cv.itemconfig(rt,text='start'))

rtags = []
for i in range(10):
    cv.create_rectangle(700, 500 + i * 30, 900, 530 + i * 30, outline='blue', fill='white', tags='r' + str(i+1))
    rtags.append('r' + str(i + 1))

fenlei(num=numbers)

root.after(4900, lambda:cv.itemconfig(rt,text='stop'))    
#root.after(5000, lambda:root.destroy())
root.mainloop()  

        #tianchong.join()
        
           
          
        
 
  
  

      
        
    #num=0
    
