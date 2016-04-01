import os
import sys
import numpy as np

def is_abnormal(recognize_result):
	abnormal = False
	results = recognize_result.split(',')
	for r in results:
		if len(r) != 1:
			#print "abnormal: " + r
			abnormal = True
			break
	return abnormal

def contain(line, mark):
	return line.find(mark) != -1

def get_data(line):
	start = line.find('>')
	end   = line.find('<')
	return line[start+1:end-start-3]



scan_record_xml_file = sys.argv[1]
file_object = open(scan_record_xml_file)
lines = file_object.readlines()

record_object = open('_record.txt', 'w')
abnormal_record_object = open('_abnormal_record.txt', 'w')

file_mark = 'Files'
omr_str_mark = 'OmrStr'
enter = '\n'

student_num = 0
abnormal_record = []
abnormal_student_image = []
fine_image_name = False
image_name = ''
for index in range(len(lines)):
	line = lines[index]
	line.strip()
	if contain(line, file_mark):
		fine_image_name = True
		image_name = get_data(line)
		student_num += 1
	if contain(line, omr_str_mark) and fine_image_name:
		recognize_result = get_data(line)

		record_object.write(image_name + enter)
		record_object.write(recognize_result + enter)

		if is_abnormal(recognize_result[0:len(recognize_result) - 1]) :
			abnormal_student_image.append(image_name)
			abnormal_record.append(recognize_result)

		fine_image_name = False
		image_name = ''

if len(abnormal_student_image) > 0 :
	for index in range(len(abnormal_student_image)):
		print abnormal_student_image[index]
		print abnormal_record[index]
		abnormal_record_object.write(abnormal_student_image[index] + enter);
		abnormal_record_object.write(abnormal_record[index] + enter);

record_object.close()
abnormal_record_object.close()

print 'students num : ', student_num
print  'abnormal num : ', len(abnormal_student_image)
