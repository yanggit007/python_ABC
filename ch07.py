# 非结构化编程  -->  机器语言，汇编语言     ---  goto满天飞，无方向，顺着机器的脾气和口味界定对象
# 结构化编程    -->   Fortran, C语言      ---  面向过程，数据和算法分开表达，人机折中界定对象
# 面向对象编程  -->  C++, Java, python   ---  以人的主观意识界定对象
# 函数式编程    -->       Lisp           ---  针对那些可被数学函数化的对象（如卫星，微观粒子运动等）
# 多范式融合：具体情况，具体界定对象

class People:  # 在类的内部，cls一律代表类本身，self代表既将被实例化的实例，自己有不用继承来的，包括init构造函数也是

    count = 0  # 类属性(People.count)

    def __init__(self, name, age):  # 1，构造函数； 2，初始化函数； 3，init方法
        self.name = name   # 实例属性（系统认为：实例属性都应该在init函数里完成，包括私有属性和受保护的属性）
        self.age = age     # 构造函数中的实例属性，不在类的dir属性方法列表中
        self._pv = 10      # 受保护的实例属性 _aaa
        self.__pv = 30     # 私有的实例属性 __aaa
        People.count += 1  # 统计实例化次数，也是类属性函数体调用方式，不能用global调用，global只能调用类外部的变量

    @property  # property把方法属性化，就是使用时不再用括号。
    def n(self):
        People.count += 1
        return self.__pv

    @n.setter  # 从外观上看，像是在实例方法之上加了一句@，相当于g(f(x))，函数外面加了个函数，实现功能增强
    def n(self, x):
        self.__pv = x
        People.count += 1

    @classmethod     # 类方法说明，没考虑带参数的情况
    def test1(cls):  # 类方法函数体可调用：类属性，类方法，静态方法，装饰器，不能调用self属性，self方法，但可调用也实例后的实例的属性和方法
        print('这是第一个类方法。')
        print(cls.count)     # 第一种调用类属性
        print(People.count)  # 第二种调用类属性
        cls.test2()          # 第一种调用类方法
        People.test2()       # 第二种调用类方法
        cls.test4()          # 第一种调用静态方法
        People.test4()       # 第二种调用静态方法
        print(someone.n)     # 调用property装饰器
        print(someone.name)  # 调用已经实例后的实例的属性
        someone.say()        # 调用已经实例后的实例的方法

    @classmethod
    def test2(cls):
        print('这是第二个类方法。')

    @staticmethod            # 就是参数中没有self，cls的方法，不用@声明的话，系统会提示这可能是个静态方法
    def test3():             # 静态方法函数体可调用：类属性，类方法，静态方法，装饰器，实例后的实例的属性和方法
        print('这是第一个静态方法。')
        print(People.count)  # 调用类属性
        People.test2()       # 调用类方法
        People.test4()       # 调用静态方法
        print(someone.n)     # 调用property装饰器
        print(someone.name)  # 调用已经实例后的实例的属性
        someone.sing()       # 调用已经实例后的实例的方法

    @staticmethod
    def test4():
        print('这是第二个静态方法。')

    def say(self):  # 实例方法函数体可调用：类属性，实例属性，类方法，实例方法，静态方法，装饰器，实例后的实例的属性和方法
        print('这是第一个实例方法。')
        print(People.count)  # 调用类属性
        People.test2()       # 调用类方法
        People.test4()       # 调用静态方法
        print(self.age)      # 调用实例属性
        self.sing()          # 调用实例方法
        print(someone.n)     # 调用property装饰器
        print(someone.name)  # 调用已经实例后的实例的属性
        someone.sing()       # 调用已经实例后的实例的方法

    def sing(self):
        print('这是第二个实例方法')


someone = People(name='Jack', age=20)
p2 = People('Tom', 25)
# print(someone.n)
# someone.n = 56
# print(someone.n)
# print(People.count)
# someone.say()
# someone.sing()
# someone.test1()
# someone.test2()
someone.test3()
# someone.test4()

print(p2, type(p2))             # 这4个很烧脑
print(People, type(People))     # globals()就很清晰了

print(globals())
