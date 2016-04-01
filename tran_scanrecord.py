import os
import sys
import numpy as np

def contain(line, mark):
	return line.find(mark) != -1

def transform(line):
	trans_line = ''
	pos1 = line.find(line, '.')
	substr = line(pos1 + 1:);
	pos2 = substr.find('<');
	if pos2 > pos1:
		trans_line = line(0:pos1) + substr(pos2 + 1 :)
	return trans_line



scan_record_xml_file = sys.argv[1]
file_object = open(scan_record_xml_file)
lines = file_object.readlines()

tran_record_object = open('scanrecord_a.txt', 'w')
enter = '\n'

for index in range(len(lines)):
	line = lines[index]
	line.strip()
	if contain(line, '.'):
		trans_line = transform(line)
		if trans_line != '':
			tran_record_object.write(trans_line + enter)
		else:
			tran_record_object.write(line + enter)
	else:
		tran_record_object.write(line + enter)

tran_record_object.close()


print 'end '
