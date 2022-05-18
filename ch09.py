"""
'r' 〜 打开已有文件读取（默认）

'x' 〜 创建一个新文件，打开，写操作，若文件已存在会报错
'w' 〜 打开已有文件去写，会抹去原有内容，没有文件会新建
'a' 〜 打开已有文件去写，在原内容后面写，没有文件会新建

'b' 〜 二进制模式      （'b'是缀在'r' 'w' 'x' 'a'后面用的）
't' 〜 文本模式（默认） （'t'是缀在'r' 'w' 'x' 'a'后面用的）

'+' 〜 打开磁盘上一个文件读写
'u' 〜 通用换行模式（已弃用）

    ***** 默认是'rt'模式，'a'模式相当于'at'模式。*****
"""
# 序列化与反序列化需要import pickle | pickle.dump(p1, f) | p2 = pickle.load(f)

from sys import stdin, stdout
import io

# 以下三句没有回车，是一行，所以会等到输出readlines值以后才会全行运行。
stdout.write('hello world%python.')
print('hello world', 'python', sep='%', end='.')
a = stdin.readlines()  # ()内无参数，执行可输入多行，输入一行，回车也是字符\n, 直到command + D结束
print('')              # stdin.readlines()之后如果用b = input('请输入：')，会报EOF错误。
print(a, type(a))
print('\n')

with open('text1.txt', 'w') as f:
    f.write('Line 1\n')
    f.writelines(['Line 2\n', 'Line 3\n'])
    f.write('第四行\n')
    f.write(r'Line 5\n')        # \n不会被转义成换行，而是被当作字符。
    f.write(r'Line 6\n')        # 非二进制模式下，f.write(b'Line 7\n')加b会报错。

h = open('text2.txt', 'wb')
h.write(b'hello world 1\n')     # 二进制模式下，字符串前面必须加b
h.writelines([b'hello world 2\n', b'hello world 3\n'])
h.close()


with open('text2.txt', 'rb') as txt:
    content = txt.read()
    print(content)
    
# 以上相当于：
# txt = open('text2.txt', 'rb')
# content = txt.read()
# print(content)
# txt.close()

g = open('text1.txt')
# 以下四种方式共用一个指针
for item in g:                  # for取文本文件，每次取一行
    print(item, type(item))
g.seek(0)                       # ()括号里的数字指针是指第一行第一个字符。
print(g.read())                 # 结果是取整个字符串，带换行的字符串。
g.seek(0)
print(g.readline())             # 结果是取了一行，作为一个字符串
print(g.readlines())            # 结果是一个字符串列表，从当前指针，每行是列表中的一个字符串
g.close()
print('\n')

k = open('text2.txt', 'rb')     # 所有文件都可用二进制形式读取，读取的字符串前面加b,否则不加b
# 以下四种方式共用一个指针
for item in k:                  # for取文本文件，每次取一行
    print(item, type(item))     # 执行结果：b'hello world 1\n' <class 'bytes'>
k.seek(0)
print(k.read())                 # 执行结果：b'hello world 1\nhello world 2\nhello world 3\n'
k.seek(0)
print(k.readline())             # 执行结果：b'hello world 1\n'
print(k.readlines())            # 执行结果：[b'hello world 2\n', b'hello world 3\n']
k.close()
print('\n')


# 类似读写文件的软操作
p = io.StringIO()
p.write('hello')
p.write(' ')
p.write('world!')
print(p.getvalue())

q = io.StringIO('Hello!\nWorld!\nWelcome!')
while True:
    s = q.readline()
    if s == '':
        break
    print(s.strip())

r = io.BytesIO()
r.write('您好'.encode('utf-8'))
print(r.getvalue())
print(r.getvalue().decode('utf-8'))

t = io.BytesIO(b'\xe6\x99\x9a\xe9\xa5\xad')
print(t.read().decode('utf-8'))


# 序列化与反序列化(pickle | json)
# import pickle
# class people:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say(self):
#         print('hello world')


# p1 = people('Jack', 20)
# print(pickle.dumps(p1))

# 序列化
# with open('ppp', 'wb') as f:
#     pickle.dumps(p1, f)

# 反序列化
# with open('ppp', 'rb') as f:
#     p2 = pickle.load(f)

# print(p2, type(p2))
# print(p2.name, p2.age)
# p2.say()
