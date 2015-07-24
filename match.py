# -*- coding: utf-8 -*-
import os
import sys
import numpy as np

"""
匹配两个txt文件中的内容，并输出相同的百分比。
用于计算识别算法的识别准确率
"""

if len(sys.argv) != 3:
	print 'please input valid param\n'
	sys.exit(-1)

print sys.argv[1]
print sys.argv[2]

filepath1 = sys.argv[1]
filepath2 = sys.argv[2];

data = np.loadtxt(filepath1)
data1 = np.loadtxt(filepath2)

num = 0
correctnum = 0
allnum = 0
for index in range(len(data)):
    if data1[index] != -1:
        num = num + 1
        #print index + 1, data1[index]

    if data[index] != -1:
        allnum = allnum + 1    
        
    if data[index] == data1[index] and data[index] != -1:
        #print index + 1, data[index]
        correctnum = correctnum + 1
    else:
    	print index + 1, data[index], data1[index]

print 'recognition num : ', num
print 'wrong reocg num : ', num - correctnum
print 'corre recog num : ', correctnum
print 'all num : ', allnum
