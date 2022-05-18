# namespace命名空间(L-E-G-B)
# built-in  系统原始命名空间，有固定名称和固定级别，不可修改，可通过dir(__builtins__)返回一个key列表。

# global 全局命名空间，有固定级别，它包含built-in的空间和全局自定义空间，可通过globals()方法返回一个字典。
# global 返回字典中，built-in只是其中的一项；(内置函数，方法不会出现在global变量中，而自建和import的会。)
#        其它项包含：1,import的模块或函数，变量；2,自定义变量；3,自定义的函数；4,自定义的类；5,类的实列化等
# global 全局将built-in的变得重新赋值时：built-in不会被改变，只能作为一个新变量放在全局中，优先调用。

# local 局部命名空间，指当前位置，可将当前位置的命名空间，通过locals()方法返回一个字典。
# local 返回字典的内容是：
#              1,若它在全局中执行，返回值与globals()返回值一样。
#              2,若它在局部，如函数或类的内部执行，返回值就是函数或类的局部空间变量

# enclosing 指处在global与local之间的命名空间，函数或类包含两层以上，它才真实存在，它没有类似locals()的方法。
# enclosing 当函数或类包含超过两层时，调用变量总是从离local最近的层开始，整体调用顺序是L-E-G-B.

# 越界修改：global x 和 nonlocal x (默认情况下：局部修改不了全局变量。)
# 在局部用 global x 和 nonlocal x 声明的变量，不属于局部，不在局部的locals()字典中。
# global x 出现在类或者函数体中，让局部local可以越界（可越过多个中间层）修改全局global变量x。
# nonlocal x 多出现在具有多层的函数体中，local可越界修改enclosing中跟当前最近层的变量，且最近层不能是全局。
# 用nonlocal x时，不管全局里有没有变量x, 但enclosing中不管第几层必须有变量x，否则报错；
# 用global x时，全局和enclosing中都没有变量x也可以；
# 全局修改不了built-in，只能再存一份，优先调用；
# 局部本来也是修改不了全局，只能再存一份，优先调用；但全局不像built-in那样牢不可破，.append修补和越界都可破例。
# dir('') == dir('aaa') == dir('__builtins__') 显示字符串（某类对象）的属性和方法。
# dir() 显示globals()字典的关键字。

print(dir(__builtins__))    # 执行结果是一个由字典的key值组成的列表，不能用append修改，自身也不会变化。
print('\n')

x = [1, 2, 3]
copyright = 'This is the global copyright.'  # built-in中什么都不会变，新赋值会出现在全局中，调用时全局优先。

print(x)
print(copyright)
print(globals())  # globals()出现在哪儿都是指当前全局中的量：1，built-in； 2，新变量； 3，函数句柄； 4，类句柄。
print(locals())   # locals()若出现在全局，跟globals()值一样；出现在局部才真正有意义，只表示局部的变量，函数等。
print('\n')


def foo():
    # globals()['x'] = [1, 2, 3, 4, 5]  # 相当于global x  ## x = [1, 2, 3, 4, 5]
    # global x, copyright
    x = 1, 2, 3, 4, 5  # 不能在赋值前引用；如先x.append,再x = 1会报错。
    copyright = 'This is the enclosing copyright.'
    
    print(x)
    print(copyright)
    print(globals())
    print(locals())
    print('\n')

    def bar():
        # nonlocal x, copyright
        x = ['a', 'b', 'c']
        copyright = 'This is the local copyright.'

        print(x)
        print(copyright)  # 优先找局部（本地local），再看enclosing, global, built-in.
        print(globals())
        print(locals())   # 只显示bar里新声明的变量。（很纯粹，价值大，写在全局里就没什么价值。）
        print('\n')

    bar()

    print(x)
    print(copyright)
    print(globals())      # 可以用globals()['key'] = value在任何局部位置为全局修改或声明变量。
    print(locals())
    print('\n')


foo()

print(x)
print(copyright)
print(globals())
print(locals())
