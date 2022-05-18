a = None
b = True
c = 'hello world'
d = (2, 0, 2.5, None, 0, True, (1, 3, 5), [2, 4, '6'], {'a', 2, 'c'}, {'a': 1, 2: 'b'}, False)
f = [2, 0, 2.5, None, 0, True, (1, 3, 5), [2, 4, '6'], {'a', 2, 'c'}, {'a': 1, 2: 'b'}, False]
g = {2, 0, 2.5, None, 0, True, (1, 3, 5), False}
h = {'a': 20, 'b': '21', 3: 'abc', 4: 99.9, None: 23, False: True, 7: None}

# i = str(a, b) 只要不像这样罗列，a, b, c, d, f, g, h，以及整数浮点数都可字符串化。
# 字符串方法：.index(), .count() .upper()
# 字符串方法：'a{name}c,d{age}e'.format(name='aaa', age=5), f'a{name}b, c{age}d.'
# 字符串传统方法：'a%s, b%dc.'%(name, age)
j = str(a)               # 执行结果：None <class 'str'>
k = str(b)               # 执行结果：True <class 'str'>
m = str(23.258)          # 执行结果：23.258 <class 'str'>
n = str(h)               # 执行结果：{'a': 20, 'b': '21', ... None: 23, False: True, 7: None} <class 'str'>

# 只要是数字，无论整数，还是浮点数，都可整数化，字符串中的字符必须是"整数型"才能整数化
# 可直接加减乘除
p = int(23.97)           # 执行结果：23 <class 'int'>
q = int('2347')          # 执行结果：2347 <class 'int'>

# 只要是数学，无论是字符串，整数，小数，23.34等都可浮点化
# 可直接加减乘除
r = float('233')         # 执行结果：233.0 <class 'float'>
s = float(233)           # 执行结果：233.0 <class 'float'>
t = float(2e3)           # 执行结果：2000.0 <class 'float'>

# 基本数据类型，只有字符串可以元组化，元组，列表，集合,字典都可元组化，字典提取key值。
# 元组方法：.index(), .count(), 可切片u[1:3]
# u = (1)相当于u = 1, u = 1, 2,相当于u = (1, 2)
u = tuple(h)             # 执行结果：('a', 'b', 3, 4, None, False, 7) <class 'tuple'>
del u                    # 可以删除整个元组

# 基本数据类型，只有字符串可以列表化，元组，列表，集合,字典都可列表化，字典提取key值。
# 列表方法：.index(), .count(), 可切片v[1:3]
# 列表方法：.append(), .insert(), .remove(), .reverse(), .sort(), .sort(reverse=True)
v = list(h)              # 执行结果：['a', 'b', 3, 4, None, False, 7] <class 'list'>
del v[2]                 # 可以删除某个元素

# 基本数据类型，只有字符串可以集合化，元组，列表不含可变项时，可集合化，字典集合化提取key值。
# 集合方法：.add(), .remove()
# 可判断：'d' in w  可计算：s1 & s2, s1 | s2, s1 ^ s2, s1 - s2, s2 - s1
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {'a', 'b', 'c'}
s4 = {1, 2}
print(s1 & s2)           # 执行结果：{3, 4}
print(s1 | s2)           # 执行结果：{1, 2, 3, 4, 5, 6}
print(s1 ^ s2)           # 执行结果：{1, 2, 5, 6}
print(s1 - s2)           # 执行结果：{1, 2}
print(s2 - s1)           # 执行结果：{5, 6}
TF1 = 'a' in s3          # 执行结果：True
TF2 = 'd' in s3          # 执行结果：False
s4.add(3)
s4.remove(3)
# s4.remove(3)           # 会报错
w1 = set(h)              # 执行结果：{False, 'a', 3, 4, None, 7, 'b'} <class 'set'>
w2 = set('1ab12a')       # 执行结果：{'b', '1', '2', 'a'}
w3 = set()               # 执行结果：set()    *** 空集合只能这样定义，包含元素才能用{} ***
del w2                   # 可以删除整个集合

# 字典是哈希表，没有字典化一说。可以通过x[key1] = 23 改value.
# 字典方法：.get(), .keys(), .values(), .items(), .pop(), .update(), .clear()
# 可判断：'d' in x  可合并：x = {**a, **b}表示a,b两个字典合并
# 字典的创建多一个函数方式 | ***** ch04_datatype.py *****
x = dict()               # 这是初始化，定义一个字典，而不是字典化。相当于x = {}
d1 = {'Name': 'Jack', 'Age': 9}
TF3 = 'Name' in d1       # 执行结果：True
TF4 = 'Amount' in d1     # 执行结果：False
print(d1['Name'])        # 执行结果：Jack   *** 不常用，若Name拼写错误会报错。
print(d1.get("name"))    # d4['Name']的替代形式，输入拼写错误时只是return为None，不会报错。
print(d1.keys())         # 执行结果：dict_keys(['Name', 'Age'])   ***** <class 'dict_keys'>
print(d1.values())       # 执行结果：dict_values(['Jack', 9])     ***** <class 'builtin_function_or_method'>
print(d1.items())        # 执行结果：dict_items([('Name', 'Jack'), ('Age', 9)])   ***** <class 'dict_items'>
v1 = d1.pop('Name')      # d1会被改，像列表的append
print(v1, type(v1))      # 执行结果：Jack <class 'str'>
print(d1, type(d1))      # 执行结果：{'Age': 9} <class 'dict'>    *****
d1.clear()               # print结果：{}
d2 = {1: 1, 2: 2}
d2[3] = 3                # print结果：{1: '1', 2: '2', 3: 3}
d3 = {1: 'a', 4: 4}      # print结果：{1: 'a', 4: 4}
d2.update(d3)            # d2会被改，像列表的append
print(d2)                # print结果：{1: 'a', 2: '2', 3: 3, 4: 4}
print(d3)                # print结果：{1: 'a', 4: 4}                        *****
d4 = {**d2, **d3}        # print结果：{1: 'a', 2: '2', 3: 3, 4: 4}    **kwargs形式
del d4[4]                # 删除某个元素
d5 = d4.copy()           # 新建PyObject，不像d5 = d4共用一个PyObject.

# 字符串，元组，列表有index, count方法
y = d.index(True)        # 元组d的True字段在index=6的位置
z = f.count(True)        # 列表f的True字段一共出现了1次

# 字符串，元组，列表都有index值，字典的这种写法括号里是key值, 只有列表和字典的a[0]值可修改。
aa = h[0]                # 执行结果：True <class 'bool'>

# 字符串，元组，列表，集合，字典都有len()值
bb = len(h)              # 执行结果：7 <class 'int'>
