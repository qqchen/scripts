# -*- coding: utf-8 -*- 
import os
import os.path
import shutil
import sys

"""
这个脚本用来将源目录下的文件copy到目标目录下，
同时支持只复制文件名包含某一字符串的文件。
"""

def copyFile(sourceFile, targetFile):
    if os.path.isfile(sourceFile):
        open(targetFile, "wb").write(open(sourceFile, "rb").read())    

def copyFiles(sourceDir, targetDir):
    print 'copyFiles'
    for filename in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, filename)
        targetFile = os.path.join(targetDir, filename)
        copyFile(sourceFile, targetFile)

def copyFilesByKeywrod(sourceDir, targetDir, keyword):
    print 'copyFilesByKeywrod'

    for filename in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, filename)
        targetFile = os.path.join(targetDir, filename)
        
        if os.path.isfile(sourceFile) and filename.find(keyword)>0:
            copyFile(sourceFile, targetFile)




if __name__ == "__main__":

    if len(sys.argv) < 3 or len(sys.argv) >4:
        print 'please input valid param:\npython filterFile.py sourceDir targetDir keyword'
        exit(-1)
       
    sourceDir = sys.argv[1]
    targetDir = sys.argv[2]
    if len(sys.argv) == 3:
        copyFiles(sourceDir, targetDir)
        exit(-1)
        
    keyword = sys.argv[3]
    copyFilesByKeywrod(sourceDir, targetDir, keyword)
