# Exception异常在python里是一个类：BaseException是所有异常的基类，BaseException直属Object的子类。
# Exception异常只要被显示，就意味着程序已经中断，不可能再去执行其它任何代码。所以要用try except提前拦截处理，才不至于程序中断退出。
# 所有异常都是一个类，可被实例化，触发实例和执行实例是两个概念，两种结果。
# try except语句：一个try，最少有一个except条件，可以有多个except条件，可有可无一个else语句，可有可无一个finally语句。
# try except语句：出现异常后，顺序匹配except条件，只要匹配，不再匹配其它except条件，立即执行finally后，跳出整个try except语句。
# try except语句：编程中可能会出现异常的语句一般都用try except来捕获，处理；以避免：1，App中断退出，2，向用户异常显示。
# try except语句：无论是系统触发，还是主动触发的异常，except都可以让它不显示出来。（相当于在显示异常之前，先执行except，并屏避异常显示出来。）
# except条件顺序：子类一定要写在父类前面，有相同父类的多个子类不分前后
# except条件顺序：虽然BaseException是基类，但except:一定要在except BaseException:的后面。
# python内置Exception异常列表：书本第148页

a = [10, 4, 3, 7, 11, 6, 0, 9, 22, '10']

try:
    b = [item for item in a if 100 % item == 0]
    print(b)

except SystemExit:         # 2
    print('System')

except KeyboardInterrupt:  # 2
    print('Key')

except ZeroDivisionError:  # 4
    print('0不能作为除数')
except ArithmeticError:    # 3
    print("Attribute")

except IndexError:         # 4
    print('Index')
except LookupError:        # 3
    print('Look')

except TypeError:          # 3
    print('数据类型错误')

except EnvironmentError:   # 3
    print('Environment')

except Exception:          # 2
    print('其它类型异常')

except BaseException:      # 1
    print('abc')

except:                    # 0
    print('End')

else:     # 没有异常的情况会进入这一句。一个try只能有一个else，这里没有elif的事。（注：没有异常跟有异常没捕获到是两回事。）
    print("没有异常")

finally:  # 不管有没有异常，都会执行此处代码。（异常显示之前会匹配完所有条件语句，except和else是先到先得，finally都会执行。）
    print("这是finally语句。")                # 通常在finally语法块中执行close()方法，确保文件会被关闭。


# raise是主动触发异常，而例如1/0导致的异常是系统自动触发的异常。
# raise主动触发异常的三种形式：
#
# >>> raise AssertionError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError
#
# >>> raise AssertionError()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError
#
# >>> raise AssertionError('abc')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: abc

try:
    raise NameError("This is a NameError.")  # raise主动触发异常，系统内置异常的Message是开放的，可用继承来的，也可用当前定义的。
except TypeError:
    print('Look at an Exception.')
except NameError:
    pass


class MyException(Exception):                # 自定义异常
    def __init__(self):
        pass

    def __str__(self):                       # 若这里不自定义，Message就像内置异常一样开放。
        return "这是一个自定义的异常。"          # 自定义了Message，取代继承来的Message。并且不能再修改。


try:
    raise MyException()                   # 自定义中有Message时，这里不能再定义Message，只能用前两种形式（带括号与不带括号的）。
except MyException as item:               # 这里的item是指异常的message，若无自定，则是继承来的Message.
    print("MyException Error!", item)

# >>> AssertionError
# <class 'AssertionError'>
# >>> AssertionError()
# AssertionError()
# >>> AssertionError('abc')
# AssertionError('abc')
#
# >>> g = AssertionError
# >>> h = AssertionError()
# >>> k = AssertionError('abc')
# >>> type(g)
# <class 'type'>
# >>> type(h)
# <class 'AssertionError'>
# >>> type(k)
# <class 'AssertionError'>
# >>> str(g)
# "<class 'AssertionError'>"
# >>> str(h)
# ''
# >>> h.__str__()
# ''
# >>> str(k)
# 'abc'
# >>> k.__str__()
# 'abc'
#
# g是类对象本身，h,k是类的实例化，isinstance只是判断实例对象与类的关系，可判断h,k与类的关系，不能判断g与类的关系。
# 很多对象都有自己的__str__方法，a.__str__()相当于str(a)
# __str__方法包含一个字符串，当要把这个对象字符串化str()时,就会显示那个字符串。


def demo(x, y):
    return x + y


try:
    print(1/0)                          # 捕捉到，执行except跳出try语句；没捕捉到，显示异常跳出try语句。
    assert(demo(3, 4) == 8)             # try里的第二个异常不会被检测。
except AssertionError as e:
    print("Assertion", e, "Error")
except NameError:
    print("其它异常")
except ZeroDivisionError:
    print("除0错误")

assert(demo(2, 3) == 5)                 # 断句。（不用raise就可触发的Assertion异常。类似一个方法。应该算系统触发。）
assert(demo(3, 4) == 7)                 # 如果这句条件不匹配，语法不会报"到达不了"。（raise就不能像这样连续raise.)
assert(demo(4, 5) == 9)


try:
    assert(demo(5, 6) == 11)
except AssertionError:
    print("There is an AssertionError.")
else:
    try:
        with open('file.log') as file:  # with as语句，上下文关系，可不用close，将打开的内容赋给file句柄。
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("这是第二个finally。")

print("全集终")
