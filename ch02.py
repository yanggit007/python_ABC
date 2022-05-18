# 基本数据类型
u = None             # None空值
w = True             # bool布尔值
x = 123              # int整数 (50000的另一种表达方式：50_000)
y = 12.3             # float浮点数
s1 = 'string'        # str字符串
s2 = b'binary'       # str二进制字符串
s3 = r'saw string'   # str原始字符串

# 进制
a = 0b1111           # 二进制
b = 0o17             # 八进制
c = 0xf              # 十六进制
print(a, type(a))    # 结果：15, <class 'int'>
print(b, type(b))    # 结果：15, <class 'int'>
print(c, type(c))    # 结果：15, <class 'int'>

# 浮点数
d = 1.2e-3
e = .4
print(d, type(d))    # 结果：0.0012, <class 'float'>
print(e, type(e))    # 结果：0.4, <class 'float'>

# 基本数据类型的计算
f = 'abc中国'
print(1 / 3)
print(1 // 3)
print(f * 5)

# 字符串的index, iterable和转义
g = 'test"中文"'
h = "test\"中文\""    # 用\放在引号前面，可以把引号当成是字符串的一部分
print(g, type(g))
print(h, type(h))
print(g[-4])         # 某个index值是什么字符？
print(h.index('e'))  # 某个字符是什么index值？
print(g.count('t'))

s1 = 'hello\n'
s2 = b'world\n'
s3 = r'raw string\n'
print(s1, type(s1))             # 执行结果：hello 这儿有换行 <class 'str'>
print(s2, type(s2))             # 执行结果：b'world\n' <class 'bytes'>
print(s3, type(s3))             # 执行结果：raw string\n <class 'str'>
for item in s1:
    print(item, type(item))     # 执行结果：h <class 'str'>
for item in s2:
    print(item, type(item))     # 执行结果：119 <class 'int'>
for item in s3:
    print(item, type(item))     # 执行结果：r <class 'str'>

# 基本数据类型转换
i = str(0b1111)
print(i, type(i))               # 执行结果：15 <class 'str'>

j = '732'
k = int(j)
v = str(k)
print(k, type(k))
print(v, type(v))

m = 'abc中国'
n = len(m)                      # 执行结果：5
print(m.upper(), n, type(n))

# 字符串格式化，None and bool
o = 'abc{}xyz, efg{}abc{}efg'.format(24, 48, '25')
print(o.upper(), type(o))

p = 23
q = '45'
r = f"abc{p}def,xyz{q}abc"
print(r.upper(), type(r))

s = None
t = s is not None
print(s, type(s))
print(t, type(t))

# 字符串特性测试
# >>> print("c:\windows\name")
# c:\windows
# ame
# >>> print(r"c:\windows\name")
# c:\windows\name
# >>> print("""
# ... How are you?
# ... I'm fine.
# ... """)
#
# How are you?
# I'm fine.
#
# >>> print("""\
# ... How are you?
# ... I'm fine.
# ... """)
# How are you?
# I'm fine.
#
# >>> 'py''thon'
# 'python'
# >>> text = ('Are you ready? Yes,'
# ... ' I am ready.')
# >>> text
# 'Are you ready? Yes, I am ready.'
# >>> word = 'Python'
# >>> word[:2]
# 'Py'
# >>> word[2:]
# 'thon'
# >>> word[:]
# 'Python'
# >>> word[4:100]
# 'on'
# >>> word[100:]
# ''
# >>> step = 'abcdefghijk'
# >>> step[2 : 8 : 2]
# 'ceg'
# >>> word[0] = 'a'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
