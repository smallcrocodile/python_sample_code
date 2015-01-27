#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
# ------------------------------------------------------------------------
# FileName:     [file_dir_copy.py]
# Purpose:      [copy dir B to A]
# ------------------------------------------------------------------------
"""

# import necessary module
import os
import shutil
from os.path import walk

oj = os.path.join
oif = os.path.isfile
oid = os.path.isdir

PathA = "D:\\PathA\\"
PathB = "D:\\PathB\\"

# ============================================================
def copy(arg, dirname, filenames):
    """
    Purpose / Usage: copy() is a func to create dir and copy file
    from PathB to PathA by recursion

    Parameter(s):@arg, @dirname, @filenames
    """
    # for showing progress
    print dirname

    # remove root dir
    diretory = dirname.replace(PathB, "")
    dirnameA = os.path.join(PathA, diretory)

    if oid(dirnameA):
        # if there is a dir in PathA then check
        # if subdirs and files are existing.
        for FILE in filenames:
            if oif(oj(dirname, FILE)) and not oif(oj(dirnameA, FILE)):
                # if not exists files then copy files to pathA
                shutil.copy2(oj(dirname, FILE), oj(dirnameA, FILE))
            elif oid(oj(dirname, FILE)) and not oid(oj(dirnameA, FILE)):
                # if not exsits dir then make dir in PathA
                os.system("mkdir %s" % (oj(dirnameA, FILE)))
    else:
        # if there is no same dir, then create the dir in PatchA,
        # and copy files
        os.system("mkdir %s" % (dirnameA))
        for FILE in filenames:
            shutil.copy2(oj(dirname, FILE), oj(dirnameA, FILE))
            # shutil.copy2 func can copy with original date
            # and time of file.

# ============================================================
if __name__ == "__main__":
    walk(PathB, copy, ())
    # call copy func recursively

