#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
# -------------------------------------------------------------------------------
# FileName:     [file_dir_compare.py]
# Purpose:      [compare dir A and B]
# -------------------------------------------------------------------------------
"""

# import necessary module
import os
import shutil
# these modules for file searching
from os.path import walk

# PathA stored some dirs and files not in PathB
PathA = "D:\\PathA\\"
PathB = "D:\\PathB\\"

# PathC for output
PathC = "D:\\PathC\\"

# ============================================================
def handle(arg, dirname, filenames):
    """
    Purpose / Usage: Handle  callback func or search each dir and file in PathA by recursion
    if the dir or file does not find in PathB then create the dir and copy files.

    Parameter(s):@arg, @dirname, @filenames
    """
    # for showing progress
    print dirname

    # remove root dir
    diretory = dirname.replace(PathA, "")
    dirnameB = os.path.join(PathB, diretory)
    dirnameC = os.path.join(PathC, diretory)

    if os.path.isdir(dirnameB):
        # if there are dirs in PathB same with PathA, then compare if files are existing.
        for file in filenames:
            if os.path.isfile(os.path.join(dirname, file)) and not os.path.isfile(os.path.join(dirnameB, file)):
                if not os.path.isdir(dirnameC):
                    os.system("mkdir %s" % (dirnameC))
                shutil.copy2(os.path.join(dirname, file), os.path.join(dirnameC, file))
            elif os.path.isdir(os.path.join(dirname, file)) and not os.path.isdir(os.path.join(dirnameB, file)):
                if not os.path.isdir(os.path.join(dirnameC, file)):
                    os.system("mkdir %s" % (os.path.join(dirnameC, file)))
    else:
        # if there is no same dir, then create the dir in PatchC, and copy files
        if not os.path.isdir(dirnameC):
            os.system("mkdir %s" % (dirnameC))
            for file in filenames:
                shutil.copy2(os.path.join(dirname, file), os.path.join(dirnameC, file))
                # shutil.copy2 func can original date and time of files.

# ============================================================
if __name__ == "__main__":
    walk(PathA, handle, 0)
    # call handle func recursively

