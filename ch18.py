# C语言的赋值方式更符合直觉想法，属静态语言；python是动态语言。
# C语言：每个变量都有自己的地址，自己的属性，自己的值；如x=1，注：x的指针是指向地址，而不是指向具体值。
# C语言：x += 1 原变量只改变值，其它（地址和属性）都不变；| y=x时，y会有一套全新的地址，属性和值。
# C语言：在向函数传值时，可通过指针，在地址和属性不变的情况下，只改变值。（*y += 1, fun(&y)),python没有这个功能。
# void change(int *y){*y += 1;}
# int x = 123;
# change(&x);
# printf(x)
#
# python: 每个变量都是字典形式，会产生PyName(Key值)和PyObject(Value值)。
# PyName包括：Key值和指向PyObject的指针。
# PyObject包括：type数据类型, value值, reference count引用次数。
# PyObject：可公用，可修补，不可修改，在python中，修改就是新建PyObject，修改就属immutable
# PyObject是一个CPython的实现，本质是一个C语言的struct(结构体)，不是python里的对象。
#
# python中 x += 1修改时: PyName会新建一个PyObject，放弃原PyObject。      （即：可修改）
# python中x.pop()修补时: 才能有唯一的机会修补PyObject。                  （即：可修补)
# python: y=x时，y会有自己的PyName，但指针会指向x的PyObject，原count会加1。（即：可公用）
# 无论对x,y任一个值进行修改，都会产生一个新的PyObject与它对应，原count会减1，没修改的那个变量值不变。
# 若只对x,y任一个值进行修补，不会产生一个新的PyObject，count也不变，只有值被加长或缩短了。[1, 2]
#
# immutable不可修补 ~ 会产生新的PyObject ~ pass by value
#   mutable可修补  ~  不产生新的PyObject ~ pass by reference
# 是不是mutable不单由数据类型来定，还要看修改方式。（如列表）
#
# 向函数传变量：C和Python默认都是新建变量或新建PyObject，但C可通过指针强行不新建，而python只有在可修补情况不新建。

# import ctypes  # 调用C语言代码时，要用的模块。
# xxx = ctypes.CDLL('lib_add.so')  # xxx.c gcc compile file

a = 12
b = 24
c = {a: b}           # 右边是PyObject，没有指针，不会指向a和b
d = [a, b]


def test1(f):
    f = f + [3]


x = [1, 2]
test1(x)             # tutorial：复制了一份PyObject，传给函数变量。
print('x =', x)


def test2(f):
    f += [3]


y = [1, 2]
test2(y)             # tutorial：传递的是原PyObject，原PyObject的值会被修改。
print('y =', y)
