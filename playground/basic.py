# coding=utf-8

'''
@Author: your name
@Date: 2020-03-31 12:53:22
@LastEditTime: 2020-03-31 21:04:30
@LastEditors: Please set LastEditors
@Description: python basic
@FilePath: /xmpytest/hi.py
'''


# 打印
print('look')
print 'python',
print 'is simple'
print '\n'


# 引号的使用
word = '使用单引号'
sentence = "使用双引号"
paragraph = """三个引号圈住一个段落：
大海啊
你全是水
骏马啊
你四条腿
。。。"""
print word
print(sentence)
print(paragraph)
print '\n'


# 变量
'''
Python有五个标准的数据类型：
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

Python支持四种不同的数字类型：
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）
'''
pa, pb, pc = 'c10lns', True, 6
print pa, pb, pc
print '\n'


# 字符串
str1 = 'abcdef'
print str1[2:4]
print str1[2:]
print str1[-4:-2]
print str1 * 2
str2 = '1234567890'
print str2[2:9:2]
print '\n'


# 列表
list1 = ['toady', 2020]
list2 = ['month', 3, 'weather', 'rainy']
print list1
print list2[2:3]
print list2[2:]
print list1 * 2
print list1 + list2
print '\n'


# 元组，相当于只读列表
tuple1 = ('work', 10, 'hour')
print tuple1
print '\n'


# 字典
dic1 = {'name': 'John', 'year': 1988, 2: True}
print dic1
print dic1[2]
print dic1['year']
print dic1.keys()
print dic1.values()
print '\n'


# 类型转换
print int(3.5)
print long('200')
print float('2.4')
print complex('1+2j')
print str(10)
print repr('hi')
print repr(['Jack', 18])
print repr({'name': 'John', 'year': 1988})
print eval('1+1')
print tuple({1:2,3:4})
print list({1:2,3:4})
print set({1:2,3:4})
print dict(a='a', b='b', t='t')
print dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print dict([('one', 1), ('two', 2), ('three', 3)])
print '\n'


# 运算符
print '运算符'
print 10/3
print 10%3
print 10.2/3
print 10.2//3
print 2**10
print True and False
print True or False
print not True
print 2 in [2, 3]
print 'a' not in ['a', 'b']
print 2 is 2
print 'a' is 'a'
print ['a'] is ['a']
print '\n'


# 分支流程语句，不支持 switch 语句
if True: print 'true'
if True:
  print('1')
else:
  print('2')
if False:
  print('A')
elif True:
  print 'B'
else:
  print 'C'
print '\n'