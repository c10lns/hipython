# coding=utf-8

'''
@Author: your name
@Date: 2020-03-31 21:06:55
@LastEditTime: 2020-03-31 21:12:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /xmpytest/playground/basic-func.py
'''
# 定义函数
def printme( str ):
  "打印任何传入的字符串"
  print str
  return
# 调用函数
printme("我要调用用户自定义函数!")


def ChangeInt( a ):
  a = 10
b = 2
ChangeInt(b)
print b # 结果是 2


# 可写函数说明
def changeme( mylist ):
  "修改传入的列表"
  mylist.append([1,2,3,4])
  print "函数内取值: ", mylist
  return
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print "函数外取值: ", mylist


#可写函数说明
def printinfo( name, age ):
  "打印任何传入的字符串"
  print "Name: ", name
  print "Age ", age
  return
#调用printinfo函数
printinfo( age=50, name="miki" )


#可写函数说明
def printinfo2( name, age = 35 ):
  "打印任何传入的字符串"
  print "Name: ", name
  print "Age ", age
  return
#调用printinfo函数
printinfo2( age=50, name="miki" )
printinfo2( name="miki" )


# 可写函数说明
def printinfo3( arg1, *vartuple ):
  "打印任何传入的参数"
  print "输出: "
  print arg1
  for var in vartuple:
    print var
  return
# 调用printinfo 函数
printinfo3( 10 )
printinfo3( 70, 60, 50 )


# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )