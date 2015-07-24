import os
import sys
import numpy as np

def copyFile(sourceFile, targetFile):
    if os.path.isfile(sourceFile):
        open(targetFile, "wb").write(open(sourceFile, "rb").read())
    else:
    	print 'not file'

if len(sys.argv) != 3:
	print 'please input valid param\n'
	sys.exit(-1)

#print sys.argv[1]
#print sys.argv[2]

filelistpath = sys.argv[1]
outputdir = sys.argv[2]
file_object = open(filelistpath)
filepaths = file_object.readlines()

#print filepaths[0]
#copyFile('D:\\dataset\\samples\\1012.jpg', 'D:\\dataset\\temp\\1\\1012.jpg')
"""
filepaths = ['D:\\dataset\\samples\\1012.jpg', 
		 'D:\\dataset\\samples\\1015.jpg',
		 'D:\\dataset\\samples\\1021.jpg',
		 'D:\\dataset\\samples\\1023.jpg',
		 'D:\\dataset\\samples\\1025.jpg']
"""

for index in range(len(filepaths)):
	#print 'src: ', filepaths[index]
	filepath = filepaths[index]
	filepath.strip()
	filepath = filepath[:-1]
	"""
	if os.path.isfile(filepath):
		print 'is file'
	else:
		print 'is not file'
	"""

	if filepath.rfind('\\') != -1:
		outputfile = outputdir + '\\' + filepath[filepath.rfind('\\')+1:]
		#print 'dst: ', outputfile
		copyFile(filepath, outputfile)
print 'copy done!'