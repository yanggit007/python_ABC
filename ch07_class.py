# 子类不重写__init__方法：实例化子类时，会自动调用父类的__init__()方法；继承
# 子类若重写__init__方法：实例化子类时，就不会调用父类的__init__()方法；不继承，直接用自己的构造函数；
# 子类若重写又需调用父类构造函数：使用super关键字（既要继承父类属性，又要增加属性）。
# 格式：super(子类自己的名称，self).__init__(父类相同参数实例，而不是相同变量，这种情况父类多般有默认参数)；
# super后面的参数:1,若父类有默认值，这里可以省略，也可以传实例值；2,若父类只是变量，这里必须传实例值，如age=25
# 子类实例化时，用子类__init__的传参格式，父类__init__里的参数自动继承，而且一定会有默认值，可直接引用。


class A:            # 没有继承时，类名称后不用加()，若加()执行效果跟没加一样，只会格式提醒，不会报错

    count = 0       # 类属性

    @classmethod    # 类方法
    def test1(cls):
        print('这是A的类方法')

    def __init__(self, name, age):    # 如果自己有构造函数，就不会继承父类的构造函数和构造函数中的属性
        self.name = name              # 实例属性（系统默认：实例属性都应该在这儿完成定义）
        self.age = age                # 构造函数中的实例属性，不在类的dir属性方法列表中
        self._pv = 10                 # 受保护的实例属性（也可以被继承，可以被实例）
        self.__pv = 20                # 私有的实例属性（也可以被继承_A__pv，可以被实例）

    def say(self):  # 实例方法
        print('这是A的实例方法')

    @staticmethod   # 静态方法
    def test2():
        print('这是A的静态方法')


class B(A):         # ()里就是要继承的父类名称

    grade = 5       # 子类属性

    @classmethod
    def test3(cls):
        print('这是B的类方法')

    # def __init__(self, name, age):  # 若没有构造函数，会继续父类的构造函数，实例化时用继承来的传参格式
    #     self.name = name
    #     self.age = age
    #     self._pv = 10
    #     self.__pv = 20

    def say(self):
        print('这是B的实例方法')

    @staticmethod
    def test4():
        print('这是B的静态方法')


a1 = A('Tom', 25)
print(a1.count)
a1.test1()
a1.test2()
a1.say()
print(dir(a1))

b1 = B('Jack', 20)
print(b1.count)
print(b1.grade)
print(b1.name)
print(b1.age)
b1.test1()
b1.test2()
b1.test3()
b1.test4()
b1.say()

print(dir(A))
# print(dir(a1))
print(dir(B))
print(dir(b1))

s = 'Chinese are great.'
print(s.upper)
print(s.upper())
help(s.upper)
t = isinstance(s, str)
print(s, type(s))
print(t, type(t))
