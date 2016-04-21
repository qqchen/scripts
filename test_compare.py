import os
import sys
import math
import numpy as np

def parse_file(file_path):
	file_object = open(file_path)
	lines = file_object.readlines()
	rate_result = []
	for index in range(len(lines)):
		res = lines[index]
		res.strip()

		line = ""
		for s in res:
			if (s >= '0' and s <= '9') or s =='.':
				line = line + s
			else:
				line = line + ' '
		info = line.split()
		if len(info) < 7:
			continue

		examid = info[0].strip()
		rate = info[2].strip()
		rate_result.append(examid + ":" + rate)
	return rate_result



if len(sys.argv) != 3:
	print 'please input valid param\n'
	sys.exit(-1)


path1 = sys.argv[1]
path2 = sys.argv[2]

rate1 = parse_file(path1)
rate2 = parse_file(path2)

threshold = 0.1
output_object = open('doubtle.txt', 'w')

print len(rate1), ", ", len(rate2)

for index in range(len(rate1)):
	examid1 = rate1[index].split(":")[0]
	r1 = rate1[index].split(":")[1]

	for ii in range(len(rate2)):
		examid2 = rate2[ii].split(":")[0]
		r2 = rate2[ii].split(":")[1]
		if examid1 == examid2:
			rd1 = float(r1)
			rd2 = float(r2)

			if abs(rd1 - rd2) > threshold and rd1 < rd2 and rd1 < 1.01 and rd2 < 1.01:
				line = examid1 + " : " + r1 + " ; " + examid2 + " : " + r2
				print line
				output_object.write(line + '\n')
			break

output_object.close()


print 'done!'