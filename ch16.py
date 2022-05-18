# Regular Expression 正则表达式，简写：regex或RE，用于字符串搜索，匹配。
# regex有POSIX和PCRE(Perl Compatible Regular Expression)两种风格。
# regex使用场景：1,文本匹配(如：匹配合法email地址)；2,密码强度格式要求；3,查找和替换
# 网站：regexone.com; regex101.com;

# raw string 原始字符串，例：s = r'123def'
# flags=re.I | flags是对匹配条件进行补充，可以省略flags=；
# flags=re.I | IGNORECASE 忽略大小写； re.M | MULTILINE 每行都算；更多可查看re原码doc；
# count=3 | 是指替换时，从第一个匹配结果算起，指定替换次数，写代码时可以省略count=；
# span=(3, 6) | index是前闭后开的区间，这里指index3到index5,总共3项，也就是6-3;
# 匹配条件叫 pattern | re.compile()方法所得结果的类型就是 <class 're.Pattern'>

# from re import search   globals()字典中会出现：'search': <function search at 0x~50>
# import re               globals()字典中会出现：'re': <module 're' from '/~/re.py'>

# >>> f   # 看第52行
# <callable_iterator object at 0x10e26db20>
# >>> type(f)
# <class 'callable_iterator'>   ## 少见的类型  # 还有ch10 <class 'generator'>
# >>> next(f)
# <re.Match object; span=(0, 3), match='foo'>
# >>> next(f)
# <re.Match object; span=(6, 9), match='bar'>
# >>> next(f)
# <re.Match object; span=(12, 15), match='ver'>
# >>> next(f)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

import re


def foo(match_object):
    ss = match_object.group(0)
    if ss.isdigit():
        return str(int(ss) * 10)
    else:
        return ss.upper()


s1 = r'foo123bar456ver789'
s2 = r'one,two,three'
s3 = r'and, your,  name,  hers,  are,same'
s4 = r'foo.10.bar.20.baz.30'

# 查找匹配系列
a = re.search(r'\d+', s1, flags=re.I)          # 匹配到第一个就结束，匹配不到结果是None
b = re.match(r'\D+', s1, re.M)                 # 必须从s1的第一个字符就匹配，否则是None
c = re.fullmatch(r'\w+', s1)                   # 匹配条件必须吻合整个字符串，否则是None
d = re.findall(r'\D+', s1)                     # 所有符合条件的字符段，以列表形式给出
f = re.finditer(r'\D+', s1)                    # 所有符合条件的字符段，在迭代器形式给出

# group分组（形式上就是给匹配条件打上括号，可以考虑给组取个名字，取名对.groupdict()方法影响大）
g = re.search(r'(\w+),(\w+)', s2)
h = re.search(r'(?P<name1>\w+),(\w+)', s2)
k = re.search(r'(?P<name1>\w+),(?P<name2>\w+)', s2)

# 查找替换（替代品不仅能是字符串，还能是函数形式）
m = re.sub(r'\d+', '&&&', s1, count=2)
n = re.subn(r'\D+', '###', s1, 3, re.I)
o = re.sub(r'\w+', foo, s4, count=4)

# 分割
p = [item.strip() for item in s3.split(',')]   # 字符串本身也有.split()分割方法
q = re.split(r',\s*', s3, maxsplit=2)          # 可以指定分割次数，不指定会全部分割

# 汇编(把匹配条件整合到一起)
r = re.compile(r'\d+', flags=re.I)
s = re.search(r, s1)
t = r.search(s1)

v = sum(range(20))
print(globals())      # 执行结果中没有系统内置函数sum和range，有没有search函数由import方式来定。
print('\n')

print(a, type(a))     # 执行结果：<re.Match object; span=(3, 6), match='123'> <class 're.Match'>
print(b, type(b))     # 执行结果：<re.Match object; span=(0, 3), match='foo'> <class 're.Match'>
print(c, type(c))     # 执行结果：<re.Match object; span=(0, 18), match='foo123bar456ver789'> <class 're.Match'>
print(d, type(d))     # 执行结果：['foo', 'bar', 'ver'] <class 'list'>
print(f, type(f))     # 执行结果：<callable_iterator object at 0x1050f73d0> <class 'callable_iterator'>

print(g, type(g))     # 执行结果：<re.Match object; span=(0, 7), match='one,two'> <class 're.Match'>
print(h, type(h))     # 执行结果：<re.Match object; span=(0, 7), match='one,two'> <class 're.Match'>
print(k, type(k))     # 执行结果：<re.Match object; span=(0, 7), match='one,two'> <class 're.Match'>

print(m, type(m))     # 执行结果：foo&&&bar&&&ver789 <class 'str'>
print(n, type(n))     # 执行结果：('###123###456###789', 3) <class 'tuple'>
print(o, type(o))     # 执行结果：FOO.100.BAR.200.baz.30 <class 'str'>

print(p, type(p))     # 执行结果：['and', 'your', 'name', 'hers', 'are', 'same'] <class 'list'>
print(q, type(q))     # 执行结果：['and', 'your', 'name,  hers,  are,same'] <class 'list'>

print(r, type(r))     # 执行结果：re.compile('\\d+', re.IGNORECASE) <class 're.Pattern'>
print(s, type(s))     # 执行结果：<re.Match object; span=(3, 6), match='123'> <class 're.Match'>
print(t, type(t))     # 执行结果：<re.Match object; span=(3, 6), match='123'> <class 're.Match'>
print('\n')

print(a)              # 执行结果：<re.Match object; span=(3, 6), match='123'>
print(type(a))        # 执行结果：<class 're.Match'>
print(a.string)       # 执行结果：foo123bar456ver789
print(a.start())      # 执行结果：3
print(a.end())        # 执行结果：6
print('\n')

print(g)              # 执行结果：<re.Match object; span=(0, 7), match='one,two'>
print(g.groupdict())  # 执行结果：{}
print('\n')

print(h)              # 执行结果：<re.Match object; span=(0, 7), match='one,two'>
print(h.groupdict())  # 执行结果：{'name1': 'one'}
print('\n')

print(k)              # 执行结果：<re.Match object; span=(0, 7), match='one,two'>
print(k.string)       # 执行结果：one,two,three
print(k.groups())     # 执行结果：('one', 'two')
print(k.group())      # 执行结果：one,two
print(k.group(0))     # 执行结果：one,two
print(k.group(1))     # 执行结果：one
print(k.group(2))     # 执行结果：two
print(k.groupdict())  # 执行结果：{'name1': 'one', 'name2': 'two'}
