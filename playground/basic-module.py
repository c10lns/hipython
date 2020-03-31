# coding=utf-8

'''
@Author: your name
@Date: 2020-03-31 21:16:23
@LastEditTime: 2020-03-31 21:24:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /xmpytest/playground/basic-module.py

当你导入一个模块，Python 解析器对模块位置的搜索顺序是：

1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
'''

import printtwice

printtwice.prtt('hi')