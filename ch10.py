from functools import reduce, wraps

t0 = 2, 5, 7, 30, 200
d0 = {1: 'a', 2: 'b', 3: 'c'}

t1 = (item for item in range(5))                        # 没有元组解析，这个对象不展开，可next(t1).
t2 = (item for item in t0)                                            # <class 'generator'>

l1 = [item * 5 for item in t0 if item < 40]                           # 列表解析
l2 = [item * 5 for item in t1 if item < 40]                           # 列表解析

d1 = {item: item**2 for item in range(5) if item % 2 == 0}            # 字典解析
d2 = {v: k for k, v in d0.items()}                                    # 字典解析

s1 = {item**2 for item in [-1, -5, 1, 2, -2]}                         # 集合解析

l3 = [item for item in map(lambda x: x * x, t0) if item % 5 == 0]     # map函数，lambda匿名函数
f1 = reduce(lambda x, y: x + y, t0)                                   # reduce函数
f2 = [item for item in filter(lambda x: x < 30, t0)]                  # filter过滤函数

t3 = (item for item in t0)               # 执行结果：<generator object <genexpr> at 0x109b54c10>
f3 = map(lambda x: x + 2, t0)            # 执行结果：<map object at 0x10df5bf70> <class 'map'>
f4 = filter(lambda x: x > 5, t0)         # 执行结果：<filter object at 0x10df5bb50> <class 'filter'>
f5 = reduce(lambda x, y: x - y, t0)      # 执行结果：-240 <class 'int'>


# 装饰器试错
def demo(k):            # 没有中间函数过渡，不会报错，但必须有return值。
    print(k.__name__)
    return k            # 1，没这句会报错。 2，没有两个return形成的特定闭环，已经不是想像中的装饰器效果了。


@demo                   # 没有两个return的闭环效果，出现@就会执行增强功能。
def add_tt(x, y, z):
    print(x + y + z)


add_tt(2, 5, 13)        # 不调用就会执行装饰器的增强功能，调用时跟装饰器没关系了，只是像普通函数一样执行原始功能。
print(add_tt.__name__)  # __name__没有被取代。
print('-------------------------------------')


# 标准装饰器
def g_func(f_func):     # 数学g(f(x))形式，把f函数传给g函数
    @wraps(f_func)      # 完善装饰器，还原f(x)的一些属性，而不至于被中间函数t(x)的属性取代。
    def trans_func(*args, **kwargs):    # 借助一个中间函数trans_func来过渡
        """
        This is trans_func's doc
        :param args:
        :param kwargs:
        :return:
        """
        print(f_func.__name__)          # 在这一部分实现对f(x)功能的增强
        print(f_func.__doc__)
        print(*args, **kwargs)          # 这里是中间函数的args，只是与f(x)的args相同而已

        return f_func(*args, **kwargs)  # 相当于让f(x) = t(x)，f(x)与中间函数t(x)有相同的参数
    return trans_func  # 相当于让t = g(x)，把中间函数t(x)作为对象传给g(x)，两个return实现闭环，不能错缺，否则不会执行原始功能。


@g_func
def test(x):  # 函数体内的功能是原始功能
    """
    This is test's doc.
    :param x:
    :return:
    """
    print(x * x * x)
    print('-------------------------------------')


test(5)       # 正常调用方式，调用才会顺序执行增强功能和原始功能。


# 带参数的装饰器（再套一层）注：h(x)与f(x)的参数只能有一方用*args, **kwargs.
def h_fun(s, u="made in China."):  # 参数类型：无参，默认参数，正常位置参数，正常关键字参数。（除*args和**kwargs外。）
    def g_fun(f_fun):              # 不应该在这一层增加功能
        @wraps(f_fun)              # 完善装饰器，还原f(x)的一些属性，而不至于被中间函数t(x)的属性取代。（如：__name__等）
        def trans_fun(*args, **kwargs):
            """
            This is trans_fun's doc.
            :param args:
            :param kwargs:
            :return:
            """
            print("It's a {}, It's {}".format(s, u))  # 这里才是功能增强部分，写在其它层，会被提前执行，无装饰器架势
            print(f_fun.__name__)
            print(f_fun.__doc__)
            print(*args, **kwargs)

            return f_fun(*args, **kwargs)
        return trans_fun
    return g_fun       # 这里必须return上层函数对象，才能形成闭环。


@h_fun('shirt')        # 相对于传入参数是：一个字符串和一个函数。（还有一个默认字符串。）
def check(x):          # 函数体内的功能是原始功能
    """
    This is check's doc.
    :param x:
    :return:
    """
    print(x + x * x)
    print('-------------------------------------')


check(5)               # 正常调用方式，调用才会顺序执行增强功能和原始功能。

print(test.__name__)   # 使用functools里的wraps方法还原f(x)的属性，避免被中间函数t(x)的属性取代。
print(test.__doc__)    # import functools时，装饰器使用方式：@functools.wraps(f_fun)
print(check.__name__)  # from functools import wraps时，装饰器使用方式：@wraps(f_fun)
print(check.__doc__)   # @wraps(f_fun)，括号里是需要被还原的函数对象，即不带括号()

print("全集终")
