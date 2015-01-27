#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# -------------------------------------------------------------------------------
# FileName:    []
# Purpose:     管理调用外部EXE文件
# Author:      [ZhouKe]
# Created:     2014 - -
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------


# -*- coding:UTF-8 -*-
import os
import subprocess


class ExeMgr(object):
    """
    Purpose / Usage: 管理调用外部EXE文件

    Parameter(s):
    """

    def __init__(self, appPath):
        """
        Purpose / Usage: 初始化方法接收 EXE文件路径

        Parameter(s): @appPath: 要启动的应用程序的路径
        """
        self.appPath = appPath
        self.pid = None
        # pid:启动的进程id


    def start(self):
        """
        Purpose / Usage:  启动应用程序, 判断应用程序路径是否存在

        Parameter(s): @None
        """
        if os.path.exists(self.appPath):
            p = subprocess.Popen(self.appPath)
            self.pid = p.pid
            if self.pid is None:
                return False
            return True

        else:
            print '应用程序路径' + self.appPath + '不存在'

if __name__ == '__main__':
    exeMgr = ExeMgr(r"C:\windows\notepad.exe")
    exeMgr.start()
    print '程序已成功启动'