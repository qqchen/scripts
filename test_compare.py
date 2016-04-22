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


def parse_file_dict(file_path):
	file_object = open(file_path)
	lines = file_object.readlines()
	rate_result = {}
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
		#rate_result.append(examid + ":" + rate)
		rate_result[examid] = rate
	return rate_result



if len(sys.argv) != 3:
	print 'please input valid param\ntest_compare.py error.txt right.txt\n'
	sys.exit(-1)


path1 = sys.argv[1]
path2 = sys.argv[2]

rate1 = parse_file_dict(path1)
rate2 = parse_file_dict(path2)

#rate1.sort()
#rate2.sort()

threshold = 0.2
output_object = open('doubtle.txt', 'w')

print len(rate1), ", ", len(rate2)
res_list = []

"""
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
				res_list.append([examid1, r1, examid2, r2, abs(rd1 - rd2)])
				del rate2[ii]
			break
"""

for k in sorted(rate1.keys()):
	key = k
	val_1 = rate1[key]

	val_2 = rate2.get(key);

	if val_2 :
		rt1 = float(val_1)
		rt2 = float(val_2)
		if abs(rt1 - rt2) > threshold and rt1 < rt2 and rt1 < 1.01 and rt2 < 1.01:
			line = key + " : " + val_1 + " ; " + key + " : " + val_2
			print line
			res_list.append([key, val_1, key, val_2, abs(rt1 - rt2)])




res_list.sort(key=lambda x : x[4], reverse=True)

output_object.write("error : right\n")

def write_file(item):
	line = item[0] + " : " + item[1] + " ; " + item[2] + " : " + item[3] + " ; " + str(item[4])
	output_object.write(line + '\n')

map(write_file, res_list)

"""
for x in range(len(res_list)):
	print res_list[x]
	line = res_list[x][0] + " : " + res_list[x][1] + " ; " + res_list[x][2] + " : " + res_list[x][3] + " ; " + str(res_list[x][4])
	output_object.write(line + '\n')
"""
output_object.close()
print 'done!'