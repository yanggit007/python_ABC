# 所有编程语言都要遵守的两条规则：1,语言结构，2,流程控制；
# 这两条规则控制了整个程序的运行步骤；
# 流程控制包括三种形式：1,按顺序控制流程，2,按条件控制流程，3,按循环结构控制流程；
# if语句的核心是：条件测试表达式，表达式有两个值：True和False；
# if语句条件测试不仅支持布尔类型，空None，数值，字符串，元组，列表，字典都可以；
# 测试表达式的值为False的情况：None, 布尔False, 数值0, 空字符串，空元组，空列表，空字典；

import random

# if语句
f = int(input('请输出一个数字：'))
if f > 0:
    print('这是一个大于0的数字。')
elif f == 0:
    print('这是0。')
else:
    print('这是一个小于0的数字。')


# while语句，以及与if对比
g = 10
while g > 0:            # 条件型循环
    print(g)
    g = g - 5           # 让条件发生变化的环节，否则成死循环
print('结束')

t = 10
if t > 0:               # 只有一遍，不会循环
    print(t)
    t = t - 1
print('结束')


# for语句，range函数的特性
k = range(1, 20, 5)
print(k, type(k))       # 执行结果: range(1, 20, 5) <class 'range'>
for v in k:             # 指针型循环，从头到尾，循环次数有限，根据对象不同，每次取一个字符，一个字段或一行等。
    print(v, type(v))


# break语句
for x in range(10):     # 每次取一个值
    print(x, type(x))
    if x % 2 != 0:
        break           # 跳出循环


# continue语句
for y in range(10):     # 取字符串时，一次一个字符；取容器数据时，一次一个字段；取文件时，一次一行。
    if y % 2 == 0:
        continue        # 再从头循环
    print(y)


# else与while, for的组合
count = 0
while count < 5:
    print(count, ' is less than 5')
    count += 1
else:                   # else只在判断语句不成立时才会执行。
    print(count, ' is not less than 5')

for item in range(5):
    print(item, 'in for segment')
    if item == 3:
        break
else:                   # 判断语句没有不成立，所以else不会执行。
    print(item, 'in for segment')


# 条件测试表达式
x1 = None
x2 = 0
x3 = 3.5
x4 = [1, 2, 3]

if x1:
    print(x1)

if x2:
    print(x2)

if x3:
    print(x3)

if x3 > 0 and (x2 < 2):  # 括号要不要都行，'and'是'与'，'or'是'或'。
    print('True')

if 2 in x4:
    print(2)


# Games
m = random.randint(1, 100)
print('random is', m)
while True:
    n = int(input('Number 1 ~ 100 : '))
    if n == m:
        print('You are right.')
        break
    elif n > m:
        print('It is too big.')
    else:
        print('It is too small.')
