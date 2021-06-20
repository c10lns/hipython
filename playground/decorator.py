from functools import wraps


# 装饰器
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('before ' + func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log
def func1():
    print("func1")


def func2():
    print('func2')


if __name__ == '__main__':
    func1()
    func2()
