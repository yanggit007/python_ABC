# ch03-1
a = [1, 2, 3]
b = [1, 'abc', 2.0, ['a', 'b', 'c']]
print(a, type(a))
print(b, type(b))
print(a[0], a[1], a[2], sep='-', end='**')  # print函数的默认参数

print('\n')

# 列表切片
c = b[1:3]
print(c, type(c))
s = 'Chinese is not so easy.'
print(s[1:3], s[-1])
print(b[-1])
v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
del v1[1]                 # 可以删除index所指的某个元素
v2 = v1.copy()            # 新建PyObject，不像v2 = v1共用一个PyObject.
v3 = v2[:]                # 新建PyObject，不像v2 = v1共用一个PyObject.
v4 = v3[2:]               # 执行结果：[4, 5, 6, 7, 8, 9, 10, 11, 12]
v5 = v4[:7]               # 执行结果：[4, 5, 6, 7, 8, 9, 10]
v6 = v5[1:6:2]            # 执行结果：[5, 7, 9]
v7 = v1[2::3]             # 执行结果：[4, 7, 10]

print('\n')

# 获取列表的一些基本信息
list1 = [9, 1, -4, 3, 7, 11, 3]
print('list1的长度 =', len(list1))
print('list1里的最大值=', max(list1))
print('list1里的最小值 =', min(list1))
print('list1里3这个元素一共出现了{}次'.format(list1.count(3)))
print(list1.index(9))

# ch03-2

# 列表的改变
lst2 = ['a', 'c', 'd']

# 给list2结尾添加一个新元素 'e'
lst2.append('e')
print('lst2=', lst2)

# 在list2的'a'和'c'之间插入一个 'b'
lst2.insert(1, 'b')
print('lst2=', lst2)

# 删除list2里的'b'
lst2.remove('b')
print('lst2=', lst2)

lst2[0] = '1'
print('lst2=', lst2)

# 列表翻转
lst3 = [1, 2, 3]
lst3.reverse()
print('lst3=', lst3)

# 列表排序
lst4 = [9, 1, -4, 3, 7, 11, 3]
lst4.sort(reverse=True)
print('lst4=', lst4)

lst5 = [1, 'a', 3, [1, 2], 'c']
# x = max(lst5)

# ch03-3

# 元组的创建
x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = [1, 2, 3],
print(x, type(x))
print(y, type(y))

# 元组的访问
print(x[1])
print(x[1:])
print(x[-1])
print(x[:7:3])
print(x[8::-2])

# ch03-4

# 获取元组的一些基本信息
tuple1 = (9, 1, -4, 3, 7, 11, 3)
print('tuple1的长度 =', len(tuple1))
print('tuple1里的最大值=', max(tuple1))
print('tuple1里的最小值 =', min(tuple1))
print('tuple1里3这个元素一共出现了{}次'.format(tuple1.count(3)))

print(tuple1.index(3))
