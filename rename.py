# -*- coding: utf-8 -*-
import os
import sys

"""
重命名所给目录下的文件名
若prefix为数字，则所有的文件名称从prefix+1开始递增
若prefix为非数字，则所有的文件名称为prefix+i,(i=1,2,3...)
"""

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print 'please input valid param:\npython rename.py path prefix'
    sys.exit(-1)

path = sys.argv[1]
prefix = ''
if len(sys.argv) == 3:
    prefix = sys.argv[2]

imgtype = ['png','jpg','bmp','tif','ppm','gif', 'PNG']
index = 1
if os.path.isdir(path):    
    for oldname in os.listdir(path) :
        if os.path.isfile(os.path.join(path, oldname)) == True:
            token = '.'
            if oldname.find(token)>0:
                filename = oldname.split(token);
                type = filename[len(filename)-1]
                #print filename
                if len(filename)>1 and type in imgtype:
                    #print type
                    if prefix.isdigit():
                        #prefixNum = (int)prefix
                        newname = str(int(prefix) + index) + '.' + type # 以prefix递增
                    else:
                        newname = prefix + str(index) + '.' + type # 以prefix为前缀
                    index = index+1
                    if cmp(newname, oldname) != 0:
                        #print oldname + ', ' + newname + ', ' + ' is different'
                        os.rename(os.path.join(path, oldname), os.path.join(path, newname))
                    #else:
                    #    print oldname + ', ' + newname + ', ' + ' is same'
                        
