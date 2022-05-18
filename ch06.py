# 函数有5种传参方式
# 1，无参； 2，正常参数； 3，默认参数； 4，位置参数*args; 5，关键字参数**kwargs
# 参数顺序：正常参数必须在最前，关键字参数必须在最后，默认参数和位置参数位置可互换
# 正常参数和默认参数可出现多次，位置和关键字参数只能出现一次，无参括号()也不能省
# 在函数体内的global a, 声明全局中的a可用于函数体内
# 函数的两个默认属性：__name__函数名字；__doc__函数的标准注释
# 标准注释只能写在函数体最前面，用三个双引号括起来

def test0():          # 无参
    """
    test0 is no arg function
    :return: None
    """
    pass


def test1(a, b):      # 位置传参 与 关键字传参 都可以
    """
    This is test1's doc
    :param a: the first arg
    :param b: the second arg
    :return: a + b
    """
    print(a, b, type(a), type(b))
    print(test1.__name__)
    print(test1.__doc__)
    return a + b


test1(2, 4)           # 位置传参，参数的个数是确定的
test1(a=3, b=9)       # 关键字传参，参数的个数确定，顺序可改变


def test2(*args):     # 只能位置传参，但参数的个数不限
    print(args, type(args))  # args是一个元组


test2(1, 2, 3)
test2(3, 2, 1)        # test2(a=1, b=2, c=3) 不能关键字传参


def test3(**kwargs):  # 只能关键字传参，但参数的组数不限
    print(kwargs, type(kwargs))  # kwargs是一个字典


test3(a=1, b=2, c=3)  # test3(1, 2, 3) 不能位置传参
test3(a=8, c=7, b=1)  # 这里不存在颠倒


def test4(a=4, b=6):  # 提前赋值，默认参数，可传可不传
    print(a + b)


test4(6)              # 不传参，位置传参，关键字传参都可以


# 正常参数， 默认参数， 位置参数， 关键字参数的顺序
def test5(y, *a, s=2, **b):  # 正常参数必须在前面， 关键字参数必须在最后， 默认和位置可颠倒
    print(y, s, a, b)


# scope作用域
x = 1
x += 1
print(x)                     # 函数体外


def test():
    global x                 # 这行打通全局，没这行，x只在函数体内有效
    x = 10
    print(x)


test()
print(x)


def tst(n):                  # 递归实现
    if n == 1:
        return n
    return n * tst(n-1)      # 自己调用自己相当于循环


print(tst(6))


def tt():
    return 3


print(tt, tt())              # tt表示在某个地址有一个函数，tt()表示函数值
print(type(tt), type(tt()))  # tt函数的数据类型是什么， tt()函数值的数据类型是什么


# 函数的注释annotations
def annotation(r: sum([1, 2, 3]),
               s: 3 ** 2,
               t: int) -> tuple:   # 必须是| -> |, 后面的tuple与真实情况不同也没关系
    result = r + s + t
    print(result)
    return result ** 2


annotation(3, 5, 7)
print(annotation(3, 5, 7))
print(annotation.__annotations__)
# {'r': 6, 's': 'args must look expression.', 't': 64, 'return': <class 'tuple'>}
