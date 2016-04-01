# -*- coding: utf-8 -*-
import os
import sys
import random

"""
打印所给目录下所有文件的路径，并写到txt文件中去
"""

if len(sys.argv) != 3:
	print 'please input valid param:\nprint_random_path.py path num'
	sys.exit(-1)

path = sys.argv[1]
num  = 1
num = int(sys.argv[2]) + 1
print path
print num

output_train = open('train.txt', 'w')
output_test = open('test.txt', 'w')

if os.path.isdir(path):
	dirs = os.listdir(path)
	random_dirs = []
	size = num;
	for x in xrange(1,num):
		index = random.randint(1, size)
		size = size - 1
		random_dirs.append(dirs[index])
		del dirs[index]

	print "size :", len(random_dirs)

	for filename in random_dirs:
		filepath = os.path.join(path, filename)
		if os.path.isfile(filepath):
			for c in filepath :
				if c == '\\' :
					output_train.write('\\' + c)
				elif c == ' ':
					output_train.write('%20')
				else:
					output_train.write(c)
			output_train.write('\n')


	for filename in dirs:
		filepath = os.path.join(path, filename)
		if os.path.isfile(filepath):
			for c in filepath :
				if c == '\\' :
					output_test.write('\\' + c)
				elif c == ' ':
					output_test.write('%20')
				else:
					output_test.write(c)
			output_test.write('\n')

output_train.close()
output_test.close()