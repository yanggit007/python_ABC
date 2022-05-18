# 3种方式：字符串格式化
# 方式1: % 占位符()； 方式2: .format占位； 方式3: f解析


# 方式1: % (%c单个字符, %d整数, %e科学计数, %E, %f浮点数, %s字符串, %%百分号，……)

# 指定长度：%5d 右对齐，不足左边补空格；(23.8 --> '   23')
#         %-5d -代表左对齐，不足右边默认补空格；(23.8 --> '23   ', %-05d同样)
#         %05d 右对齐，不足左边补0. (23.8 --> '00023')

f0 = 23.8
print('%5d' % f0)                                           # 执行结果：   23
print('%05d' % f0)                                          # 执行结果：00023
print('%-5d' % f0)                                          # 执行结果：23   |
   
# 浮点数：%f 默认是输出6位有效数据，会进行四舍五入；
#       %.2f 保留小数点后2位；
#       %6.2f 6代表整个浮点数的长度，包括小数点和小数；2代表小数的位数
#             只有当字符串的长度大于6位才起作用，不足6位空格补足，可以用%06.2使用0补足空格

f1 = 1.987656789
print('%f' % f1)                                            # 执行结果：1.987657
print('%.2f' % f1)                                          # 执行结果：1.99
print('%6.2f' % f1)                                         # 执行结果：  1.99
print('%06.2f' % f1)                                        # 执行结果：001.99
print('%-06.2f' % f1)                                       # 执行结果：1.99  |

# \t 取table制表符的含义，用于对齐，就像\n一样，跟在任意字符后面都可以，试图保持4个空格一组
print('AAAAA %d\t BBB %s\t CC\t CC' % (8, 'X'))             # 执行结果：AAAAA 8  BBB X   CC      CC

# .isdigit() | 字符串专用方法，用来判断是不是数字型(得是整数，1.2或1 2都是False)字符串；
# .strip() | 去掉字符串首尾的空格，strip有撕掉包装的意思，在正则里面出现过；
# .split(',') | 以参数字符串为界，把字符串分割成多段，多段字符串构成一个列表；
s1 = r'and, your,  name,  hers,  are,same'
s2 = [item.strip() for item in s1.split(',')]

print('%% %c %d %.2e %.3f %s %%' % (65, 65, 65, 65, '65'))  # 执行结果：% A 65 6.50e+01 65.000 65 %
s3 = '%s' % 65                                              # 测试结果：65 <class 'str'>
s4 = '%%, %s, %s, %%' % (65, '65')                          # 测试结果：%, 65, 65, % <class 'str'>


# 方式2: .format占位

name = "可优"
lover = "柠檬小姐姐"
print("{}爱上了{}！".format(name, lover))

pi = 3.14159265359
print("圆周率（{:.5f}）有多长，爱你就有多深！".format(pi))

print("{:😍^20}".format("【爱的誓言】"))

self_info = {"name": "可优", "age": 17, "lover": "柠檬小姐姐"}
print("姓名: {name:💕<6}\n芳年: {age:💕<6}\n爱人: {lover:💕<6}".format(**self_info))

f2 = 'abc{2}xyz, efg{0}abc{1}efg'.format(100, 200, '300')   # 按index
print(f2.upper(), type(f2))

print('姓名是：{0:*^11}\n年龄是：{1:*>11}'.format('Tom', 20))


# 方式3: f解析

name = "可优"
lover = "柠檬"
sea = "🌊"
tortoise = "🐢"
print(f"{name}对{lover}的爱，犹如滔滔江水！{sea * 3}\n如果加一个期限，是{500+9500}年！{tortoise * 3}")

p = 23
q = '45'
r = f"abc{p}def,xyz{q}abc"
print(r.upper(), type(r))

self_info = {"name": "可优", "age": 17, "lover": "柠檬小姐姐"}
print(f"姓名: {self_info['name']}\n芳年: {self_info['age']}\n爱人: {self_info['lover']}")

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
