# 经典图表：左列是元类，中列是类，右列是实例；左右关系是实例化关系。中列上下是继承关系。
# 从左往右看，中列的类都是左列元类的实例化对象，右列实例都是中列类的的实例化对象。
# 站在左列type的角度，从实例关系来看，一切都是对象，包括type自己，它是实例关系的顶层，而且type自己是自己的实例。
# 站在中列object的角度，中列其它类都是子类，包括左列的元类type也是它的子类，object是继承关系的顶层，它没有基类。
# 左列元类和中列类都有.__bases__属性，用来查看基类；.__bases__是类的属性，右列实例无.__bases__属性。
# type方法()：用来查看对象的类型。如：type(int)，跟int.__class__功能相同。只有整数不能用12.__class__
# 函数是对象，不是类，所以有.__class__，没有.__bases__
# 元类和类即是类又是对象：isinstance(a, (A, B, C))

# 装饰器property: 实现方法属性化，类中定义的无参函数才能用，使用时方法当属性用，不用像方法那样加括号。

# 魔法函数被实例调用时：(魔法函数都是系统定义的专用形式，专用字段，每个魔法函数都有自己特有的性质。比如__init__)
#                   方式1, a.__xxx__方法句柄：表示查看方法的自我介绍（存储地址，方法名称，所属类名称）；
#                   方式2, a.__xxx__()第一种使用方法的功能。
#                   方式3, xxx(a)第二种使用方法的功能。
#                   (私自定义__xxx__型函数，不可用第三种方式，前两种方式没有区别。）
#                   有些魔法函数需要定义才能用，如__len__; 有些不用定义就自代默认值，如__str__, __repr__
#                   魔法函数：本身就有相应功能，对它再定义可以完善和增加功能，相当于加装饰器

# __str__和__repr__相当于展示对象document的方法，默认值是存储地址，所属类名称，可以用函数重新定义。
# __str__和__repr__的区别：__str__只面向用户，优先级低。
#                        只重新定义repr时，两属性公用；
#                        只重新定义str时，只有__str__会使用；
#                        两者都重新定义时，各用各的。
# print(实例）时，默认显示的就是实例的__str__()方法定义的文档。

# 类实例化之后，还可以增加类属性和实例属性。如：Student.xx = 5, s1.xxx = 6
# 实例没有的属性，会自动到类属性里去找，找到只是引用；
# 实例若重新给这个属性赋值，将发生本质变化，不再是引用而是实例属性。（各是各的属性，相互没关系了）
# 实例若给这个属性用.append进行修改，这算引用，不算赋值，不会发生本质变化；跟函数的L-E-G-B类似。

# 交互式运行：python3.9 -i ch15.py  ## ctrl + d 退出交互式运行。

# abc抽象基类abstract base class：子类继承时，强制一定要实现父类的全部方法，起到规范子类的作用。(用不了？)

# from abc import ABCMeta, abstractclassmethod
# class Base(metaclass=ABCMeta):
#     @abstractclassmethod  # Python 3.3. Use 'classmethod' with 'abc.abstractmethod' instead
#     def read(self):
#         pass
#     @abstractclassmethod
#     def write(self):
#         pass

def my_add(x, y):
    """This is a my_add function."""
    return x + y


a = my_add                          # 函数句柄，是一个对象
l1 = [1, 2, a, my_add]
b = l1[2](2, 5)
c = l1[3].__call__(20, 30)


def test(f, x, y):
    return f(x, y)


d = test(a, 8, 9)


class Account:

    z = 1

    def __init__(self, name, amount=0):
        self.name = name
        self.amount = amount
        self.__trans = []

    def add_trans(self, x):
        self.__trans.append(x)

    @property                       # property把方法属性化
    def balance(self):
        return self.amount + sum(self.__trans)

    def __len__(self):
        return len(self.__trans)

    def __str__(self):
        return f'This is the {self.name}.account.'

    def __repr__(self):
        return f'This is for {self.name}.security.'
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance


Jack = Account('Jack', 100)
Jack.add_trans(500)
Jack.add_trans(500)
Jack.add_trans(-100)
Jack.add_trans(200)
print(len(Jack))                    # 执行结果：4
print(Jack.__str__())               # 实现方法的功能
print(repr(Jack))                   # 执行结果：This is for Jack.security.
print(Jack.balance)                 # 执行结果：1200

Paul = Account('Paul', 200)
Paul.add_trans(300)
Paul.add_trans(-200)
Paul.add_trans(1000)
print(len(Paul))                    # 执行结果：3
print(Paul.__str__)                 # 方法句柄：查看方法的自我介绍
print(Paul.__repr__)                # 执行结果：<bound method Account.__repr__ of This is for Paul.security.>
print(Paul.balance)                 # 执行结果：1300

print(Jack == Paul)                 # 有前面的魔法函数支撑，这里才能如此简洁。
print(Jack < Paul)

# print(dir(Account))
print(hasattr(Account, '__len__'))  # 执行结果：True    # 查看类有没有某个方法或属性
print(hasattr(Account, 'len'))      # 执行结果：False
print(hasattr(Account, 'name'))     # 执行结果：False   # 类的dir中有的属性才算，构造函数创建的属性不在类的dir列表中。
print(hasattr(Account, 'balance'))  # 执行结果：True
print(hasattr(Account, 'z'))        # 执行结果：True    # 类属性
