import os
import sys
import numpy as np

def contain(line, mark):
	return line.find(mark) != -1

def get_data(line):
	start = line.find('>')
	end   = line.find('<')
	return line[start+1:end-start-3]



scan_record_xml_file = sys.argv[1]
file_object = open(scan_record_xml_file)
lines = file_object.readlines()

user_object = open('students.txt', 'w')

userid_mark = 'Userid'
file_mark = 'Files'
enter = '\n'

student_num = 0
find_userid = False
userid = ''
for index in range(len(lines)):
	line = lines[index]
	line.strip()
	if contain(line, userid_mark):
		find_userid = True
		userid = get_data(line)
	if contain(line, file_mark) and find_userid:
		image_files = get_data(line)

		line = userid + ":" + image_files + enter;
				

		user_object.write(line)

		find_userid = False
		userid = ''

user_object.close()
