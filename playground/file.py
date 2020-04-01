# coding=utf-8

'''
@Author: your name
@Date: 2020-04-01 17:46:40
@LastEditTime: 2020-04-01 18:05:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /hipython/playground/file.py
'''

import time
import os

fo = open('f.txt', 'w+')

print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace

fo.write(str(time.asctime(time.localtime())))
print "当前位置：", fo.tell()

fo.seek(-4, 1)
print fo.read()

fo.seek(0, 0)
print fo.read()

fo.close()

print "是否已关闭 : ", fo.closed

os.rename('f.txt', 'ff.txt')
os.rename('ff.txt', 'f.txt')
# os.remove('none.txt')