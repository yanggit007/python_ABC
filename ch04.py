from collections import namedtuple, deque, defaultdict, Counter, OrderedDict

# 基本数据类型
Base1 = None
Base2 = True
Base3 = 123
Base4 = 123.45
Base5 = '1a2b3c'      # ***** f = b'1a2b3c' | f = r'1a2b3c' ***** #

# 数据集合类型(容器数据类型Container Datatype)
CD1 = (1, 2, 3, 'd')
CD2 = ['a', 2, 3, 'd']
CD3 = {1, 'b', 3}
CD4 = {1: 'a', '2': 'b', 'c': 3}

# 容器数据类型替代方案 | namedtuple, deque, defaultdict, Counter, OrderedDict
Student = namedtuple('Student_namedtuple', ['name', 'age'])    # print结果：<class '__main__.Student_namedtuple'>
CDA1 = Student('Paul', 25)                                     # print结果：Student_namedtuple(name='Paul', age=25)
CDA2 = deque([1, 2, 3, 4, 5])                                  # print结果：deque([1, 2, 3, 4, 5])
CDA3 = defaultdict(int)                                        # print结果：defaultdict(<class 'int'>, {})
CDA4 = Counter('adfaaedfd')                                    # print结果：Counter({'a': 3, 'd': 3, 'f': 2, 'e': 1})
CDA5 = OrderedDict()                                           # print结果：OrderedDict()

# 取字典key值 方法1：
for item in CD4:
    print(item, type(item))          # 执行结果：1 <class 'int'>

# 取字典key值 方法2：
for item in CD4.keys():              # CD4.keys()的形式：dict_keys(['Name', 'Age']) <class 'dict_keys'>
    print(item, type(item))          # 执行结果：1 <class 'int'>

# 取字典value值
for item in CD4.values():            # CD4.values()的形式：dict_values(['Jack', 9]) <class 'builtin_function_or_method'>
    print(item, type(item))          # 执行结果：a <class 'str'>

# 以元组形式，取字典key-value值
for item in CD4.items():             # CD4.items()的形式：dict_items([('Name', 'Jack'), ('Age', 9)]) <class 'dict_items'>
    print(item, type(item))          # 执行结果：(1, 'a') <class 'tuple'>

# 取字典key-value值，分别赋予x, y
for x, y in CD4.items():
    print(x, type(x))                # 执行结果：1 <class 'int'>
    print(y, type(y))                # 执行结果：a <class 'str'>

# 几种定义字典的格式
d1 = {
    1: 'a',
    2: 'b',
    '3': 'c',                        # 这里可以用逗号，也可以不用。
}
d2 = {4: 'e', 5: 'f', 6: 'g'}
d3 = dict(a=11, b=22, c=33)
d4 = dict()

d3['d'] = 44
d3['c'] = 333
print(d3['c'])                       # 执行结果：333

tuple1 = ('Name', 'Age', 'Class')
s1 = dict.fromkeys(tuple1)           # 执行结果：{'Name': None, 'Age': None, 'Class': None}
s2 = dict.fromkeys(tuple1, 15)       # 执行结果：{'Name': 15, 'Age': 15, 'Class': 15}
del s1['Class']                      # 删除某个元素
s3 = s2.copy()                       # 新建PyObject，不像s3 = s2共用一个PyObject.
