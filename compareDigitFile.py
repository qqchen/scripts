import os
import sys
import numpy as np

if len(sys.argv) != 3:
	print 'please input valid param\n'
	sys.exit(-1)

print sys.argv[1]
print sys.argv[2]

filepath1 = sys.argv[1]
filepath2 = sys.argv[2];

data1 = np.loadtxt(filepath1)
data2 = np.loadtxt(filepath2)

samedigitnum = 0

if len(data1) != len(data2):
	print 'error'
	sys.exit(-1)

for index in range(len(data1)):
	if data1[index] == data2[index]:
		samedigitnum = samedigitnum + 1
	else:
		print str(index) + ' : ' + str(data1[index]) + " , " + str(data2[index])

print 'same digit num : ', samedigitnum