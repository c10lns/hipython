# if 表达式
def fun1(flag):
    print('a' if flag else 'b')


if __name__ == '__main__':
    fun1(True)
    fun1(False)
