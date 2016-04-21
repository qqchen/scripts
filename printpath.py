# -*- coding: utf-8 -*-
import os
import sys

"""
打印所给目录下所有文件的路径，并写到txt文件中去
"""

"""
def compare(x, y):
    stat_x = os.stat(DIR + "/" + x)
    stat_y = os.stat(DIR + "/" + y)
    if stat_x.st_ctime < stat_y.st_ctime:
        return -1
    elif stat_x.st_ctime > stat_y.st_ctime:
        return 1
    else:
        return 0
"""

if len(sys.argv) != 2:
	print 'please input valid param:\nprintpath.py path'
	sys.exit(-1)

path = sys.argv[1]
print path

output_object = open('filepath.txt', 'w')

"""
if os.path.isdir(path):
	for filename in os.listdir(path):
		filepath = os.path.join(path, filename)
		if os.path.isfile(filepath):
			for c in filepath :
				if c == '\\' :
					output_object.write('\\' + c)
				elif c == ' ':
					output_object.write('%20')
				else:
					output_object.write(c)
			output_object.write('\n')
			#output_object.write(os.path.join(path, filename) + '\r\n')

output_object.close()
"""

if os.path.isdir(path):
	for filename in os.listdir(path):
		print filename
		filepath = os.path.join(path, filename)
		if os.path.isdir(filepath):
			for file in os.listdir(filepath):
				output_object.write(filename + ':')
				# linux
				#output_object.write(os.path.join(filepath, file))
				#output_object.write('\n')

				#win
				win_path = os.path.join(filepath, file)
				for c in win_path :
					if c == '\\' :
						output_object.write('\\' + c)
					elif c == ' ':
						output_object.write('%20')
					else:
						output_object.write(c)
				output_object.write('\n')
output_object.close()













































