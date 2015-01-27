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
# multiprocessing.py
from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc1(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
    time.sleep(60)


def run_proc2(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
    time.sleep(60)


def run_proc2(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
    time.sleep(60)

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    time.sleep(40)
    p.join()
    print 'Process end.'