# -*- coding: utf-8 -*-
"""1、2、3、4 组成3位数，且不能有重复的数字~！"""

#import os
#print (os.path.abspath('.'))
#/Users/figo/PycharmProjects/Study

"""f = open(file='/users/figo/desktop/test.txt',mode='w')
f.write("Alex CEO 6000\n")
f.write("黑姑娘 行政 9000\n")
f.close()
"""

f = open(file='/users/figo/desktop/test.txt',mode='r')
#print(f.readline())test.py:14
print("---------分隔符-----------")
data = f.read()
print(data)
f.close()