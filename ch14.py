# collections是python的内置模块，属于container datatype，多半是继承tuple, list, set, dict而来。
# 这个模块实现了专门的容器数据类型，提供了Python通用内置容器(dict、list、set和tuple)的替代方案。
# 容器数据类型的每一项叫做一个字段field，每个字段field都有自己的名称，位置，值。（fields in the container)

# namedtuple: 它是一个函数，用于创建具有指定字段的元组子类。(creating a tuple subclasses with named fields.)
# deque: 类似列表，列表式双向队列，前端后端都可添加和删除。
# default_dict: 定义一个value值被初始化了的字典，value的初始值由吸入的参数来决定。
#               无参数时相当于参数是None，Value值不会被初始化，只是一个空字典；
#               参数是自定义函数句柄时，value的初始值是函数的return值。int句柄的默认值是0，float是0.0, str是'', list是[], ……
# Counter: 像default_dict一样，继承字典。统计hashable对象的个数，以字典格式展示出来。
# OrderedDict: 有序字典，继承字典。定义了一个按赋值顺序排列的字典。

# a = [item for item in map(str, [1, 3, 5, 'abc', 'xx'])]
# b = list(map(str, (1, 3, 5, 'abc', 'xx')))
# tuple sequences unpacking: c, d, *vv, h = my_tuple  # (*vv p 3 4 5), (vv=[3, 4, 5])

import time
from collections import namedtuple, deque, defaultdict, Counter, OrderedDict

# namedtuple 可以定义一个特殊元组的函数
# namedtuple(指定元组)：第一参数，是namedtuple函数定义的一个新的容器数据类型的名称，类似class。
# 第二参数，可以是元组形式，列表形式，或集合形式，每个字段必须用引号，相当于属性名称或关键字。
# namedtuple函数定义了一个叫like_class的容器数据类型，当前这个具有两个字段数据的名称是Student。
Student = namedtuple('like_class', ['name', 'age'])  # 定义了一个叫Student的like_class数据类型。
s1 = Student('Alex', 30)                             # 相当于类的实例化，上面的 'like_class' 用 'class' 会报错，不能占用专用字。
s2 = Student('Paul', 25)                             # 实例后是一个元组，只能访问不能更改。class实例后可更改。
s3 = Student(30, 40)                                 # type of s3 is <class '__main__.like_class'>
t = s1[1] + s2.age + s3[0] + s3.age                  # 通过属性.age和索引[]的方式都可访问value
print(t)
print(s1)                       # 执行结果：like_class(name='Alex', age=30)
print(Student.__name__)         # 执行结果：like_class
print(Student.__doc__)          # 执行结果：like_class(name, age)
print(Student)                  # 执行结果：<class '__main__.like_class'>   # 也是s1的type


# deque 可以定义一个特殊列表的函数
d = deque([1, 2, 3, 4, 5], 20)  # 第一参数只要是iterable就行，通常写成列表形式，第二默认参数值是None, 这里写成maxlen=20也行。
d.append(6)
d.appendleft(0)                 # 列表没有向左append, extend, pop的方法
d.extend([7, 8])
d.extendleft([-1, -2, -3])      # 按照给定顺序一项一面往前插，实际效果跟直观相反。
d.pop()
d.popleft()
d.reverse()
d.insert(22, 99)                # index不够22项时，不会报错，而会插入到最后。
print(d)                        # type of d is <class 'collections.deque'>

# deque and list performance pk
t1 = time.time()
l1 = list(range(10000000))
l1.insert(111, 9999)
l1.reverse()
print(l1[599999])
print('list.time:', time.time() - t1)

t2 = time.time()
d1 = deque(range(10000000))
d1.insert(111, 9999)            # deque有明显优势的项，其它基本无优势。
d1.reverse()
print(d1[599999])
print('deque.time:', time.time() - t2)


# default_dict 继承字典的一个value被初始化的子类，无参时相当于输入None，value不会被初始化。
k = defaultdict()
m = defaultdict(None)
n = defaultdict(bool)           # type of n is <class 'collections.defaultdict'>
i = defaultdict(int)
print(k)            # 执行结果：defaultdict(None, {})
print(m)            # 执行结果：defaultdict(None, {})
print(n)            # 执行结果：defaultdict(<class 'bool'>, {})
print(i)            # 执行结果：defaultdict(<class 'int'>, {})

# print(k['a'])     # value没有被初始化，相当于一个空字典。会报异常：KeyError: 'a'
# print(m['b'])     # 同上
print(n['c'])       # 所有value值默认都是False
print(i['d'])       # 所有value值默认都是0

k['a'] = 1          # 可随意赋值，它没有被初始化。
m['b'] = [1, 2, 3]  # 可随意赋值，它没有被初始化。
n['c'] = True       # 默认值是False。
i['d'] = 'ABC'      # 默认值是0，重新赋值类型不对会有提示，但赋值都可正常执行。

print(k)            # 执行结果：defaultdict(None, {'a': 1})
print(m)            # 执行结果：defaultdict(None, {'b': [1, 2, 3]})
print(n)            # 执行结果：defaultdict(<class 'bool'>, {'c': True})
print(i)            # 执行结果：defaultdict(<class 'int'>, {'d': 'ABC'})

f = ['is', 'it', 'who', 'where', 'is', 'it', 'is', 'who']
result_1 = {}
for word in f:
    if word not in result_1:
        result_1[word] = 1
    else:
        result_1[word] += 1
print(result_1)

result_2 = {}
for word in f:
    result_2.setdefault(word, 0)  # 知识点：字典的setdefault()方法，第二参数可以是任意整数。
    result_2[word] += 1
print(result_2)

result_3 = defaultdict(int)
for word in f:
    result_3[word] += 1
# 自定义函数句柄的执行结果形式：defaultdict(<function demo at 0x102e30d30>, {})
print(result_3)  # 执行结果：defaultdict(<class 'int'>, {'is': 3, 'it': 2, 'who': 2, 'where': 1})


# Counter 继承字典的一个子类
c = Counter(f)
print(c)                   # 执行结果：Counter({'is': 3, 'it': 2, 'who': 2, 'where': 1})

p = Counter('Chinese')     # type of p is <class 'collections.Counter'>
print(p.most_common(3))    # top N 操作，出现次数统计都是从高到低。
print(p)
p.update('Japanese')
print(p)


# OrderedDict 继承字典的一个子类。(跟q = dict()没区别；赋值本来就是有序的。)
q = OrderedDict()          # type of q is <class 'collections.OrderedDict'>
q['a'] = 1
q['b'] = 2
q['c'] = 3
q.update(d=4, e=5)
print(q)
q.move_to_end('c', False)  # bool的默认值是True.
print(q)
