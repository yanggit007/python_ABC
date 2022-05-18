# python网站：www.python.org                   (chapter 1)
# pycharm网站：www.jetbrains.com/pycharm/      (chapter 1)
# VSCode网站：code.visualstudio.com            (chapter 1)
# python package index网站：pypi.org           (chapter 8)
# https://docs.python.org/3/library/logging.html#logrecord-attributes  (chapter 13)
# 正则测试网站：regexone.com | regex101.com     (chapter 16)
# git官网：https://git-scm.com
# github网站：https://github.com | github.com/docker/compose | github1s.com/docker/compose
# manim教程：github.com/cai-hust/manim-tutorial-CN
# 第三方python程序打包工具：pyinstaller
# Win: pyinstaller.exe sha256.py -F | Mac: pyinstaller sha256.py (-F打包成单个文件而不是文件夹)

# python在1991年诞生，发明人：Guido Van Rossum 荷兰人，源自1989年圣诞节的想法。
# python的底层是C语言，相当于把C语言封装后，用python语法来调度。

# python不像C++在运行之前，先通过编译器生成二进制文件，之后再运行二进制文件。
# python是动态类型的解释型语言，运行时：才进行数据类型检查，解释器将代码逐行解释为机器码，随即运行。
# python虽归类为脚本语言，但相较Shell Script，VBScript只能处理简单任务，python能处理所有计算机任务。
# python也是“胶水语言”，可集成封装其实语言编写的模块；（如用C++写对性能要求极高的部分，然后用python粘合。)
# 反过来：python编译器也可被集成到其他需要脚本语言的程序内。

# 计算公式用圆括号括起来，以便将代码分成两行，遵循每行不超过79字符的建议。（235）

# python格言：import this | this.py是一段被转化过的文本。内有print语句，import导入即展示。

# python 0 | 1991.02.20 ~ python 0.9.0  ---  1993.07.29 ~ python 0.9.9
# python 1 | 1994.01.10 ~ python 1.0.0  ---  2000.09.05 ~ python 1.6.0
# python 2 | 2000.10.16 ~ python 2.0.0  ---  2010.07.03 ~ python 2.7.0
# python 3 | 2008.12.03 ~ python 3.0.0  ---  2021.06.28 ~ python 3.9.6

# Win: 系统默认没有安装python | Mac: 系统默认安装python 2.7.16

# python3.9 -m pdb xx.py 命令行直接进入pdb模式调试xx.py文件。（xx.py内无需调用pdb.set_trace()方法。）
# python3.9 -m venv xxx  命令行创建虚似环境，其中的venv是必须的。xxx是总文件夹名字。
# python3.9 -i xx.py     命令行进入交互式执行模式。

# 课程提到的模块：os sys random pickle pdb doctest unittest
# 课程提到的模块：functools logging collections time re hashlib ctypes
# 课程提到的模块：time datetime calendar _thread threading subprocess multiprocessing

# import os时，提到的命令：dir(os), help(os.mkdir)
# os.getcwd(), os.listdir(), os.mkdir('demo'), os.path.isdir('demo'), os.chdir('demo')
# os.path.exists('text1.txt'), os.path.join('路径', 'text.txt')

# 运算符及优先级：课本30 〜 36页。% ** // != >= += *= %= **= //= & ~ << >> and or not is in
# 少见的类型：ch16 <class 'callable_iterator'>, ch10 <class 'generator'> 都可next().

# 容易忽略或忘记，却很好用的内容：
# hasattr(__obj: object, __name: str) -> bool
# hasattr(s1, 'name')     属性或方法的名称，得像这样是字符串形式
# isinstance(a, (A, B, C))
# 'ba' in 'banana'
# 15 - 7 is 8
# 15 - 7 == 8
# assert(15 - 7 == 8) | assert有断言的意思，它的行为是触发异常或不触发异常；
# '1234'.isdigit() |    字符串专用方法，用来判断是不是数字型(得是整数，1.2或1 2都是False)字符串；
# type(a) 相当于 a.__class__
# People.__bases__      多般类用这个属性来查看基类，函数和实例没有这个属性；
# >>> int.__base__
# <class 'object'>
# >>> int.__bases__
# (<class 'object'>,)
# >>> int.__class__
# <class 'type'>

# ch01: python简介
# ch02: 基本数据类型
# ch03: 元组与列表
# ch04: 集合与字典
# ch05: 条件语句和循环语句
# ch06: 函数
# ch07: 类-面向对象
# ch08: 模块和包
# ch09: 文件输入输出(I/O) pickle
# ch10: 高阶函数
# ch11: 异常处理
# ch12: 程序调试 pdb doctest unittest
# ch13: 日志记录 logging
# ch14: 容器数据类型 collections
# ch15: python底层架构(类-魔法函数-命名空间)
# ch16: 正则表达式 re
# ch17: python打包
# ch18: 调用c语言代码 ctypes
# ch19: 日期与时间
# ch20: 进程与线程
