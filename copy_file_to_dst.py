# -*- coding: utf-8 -*-
import os
import sys
import numpy as np

"""
挑选某一个目录下跟源目录同名的文件并拷贝到目标目录
"""

def copyFile(sourceFile, targetFile):
    if os.path.isfile(sourceFile):
        open(targetFile, "wb").write(open(sourceFile, "rb").read())
    else:
    	print 'not file'

if len(sys.argv) != 4:
	print 'please input valid param:\nprintpath.py path'
	sys.exit(-1)

path = sys.argv[1]
srcpath = sys.argv[2];
dstpath = sys.argv[3];
print path
print srcpath
print dstpath

if os.path.isdir(path):
	for filename in os.listdir(path):
		srcfilepath = os.path.join(srcpath, filename)
		if os.path.isfile(srcfilepath):
			dstfilepath = os.path.join(dstpath, filename)
			copyFile(srcfilepath, dstfilepath)
			print "copy file : ", srcfilepath

print "end copy"