"""
    ***** test_math.py是chapter12的单元测试部分 *****
"""
# print调试方式：写了调完再删。
# pdb调试方式：1，import pdb的set_trace()方法；2，命令行python3.9 -m pdb xx.py
# pdb调试方式：pycharm只能import进入pdb模式，命令行两种进入方法都可以
# pdb调试命令：?命令列表；l或list执行代码及上下文代码显示；s或step逐行执行（包括调用部分）；n或next一块一块执行；p打印某个变量；exit退出。
# pycharm的调试：1，未设置断点，执行到底；2，有多个断点时，执行到最先遇到的断点；3，只有一个断点时，执行到断点位置，当前行未执行。
# pycharm的调试：button1:代码内逐行执行，不进入子体；button2:逐行执行代码内外的所有子体；button3:逐行执行代码内的所有子体。
# pycharm的调试：有异常行前会有雷电符号指示。

# from pdb import set_trace
# set_trace()
numbers = [1, 2, 3, 4]


def all_even(num_list):

    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.extend([number])     # extend需要接受一个列表

    return even_numbers


all_even(numbers)
a = all_even(numbers)
print(a)
b = input('please input: ')
print(b)


# 文档测试：只要标准文档里有>>>符号，pycharm的run '文件名'就会变成：run 'Doctests in 文件名'。所有>>>行都会高亮显示。
# 文档测试：pycharm会自动检测(文档中有无>>>内容)，若检测到，默认会替代程序中的doctest.testmod()方法。
# 文档测试：VSCode和命令行，必须通过代码中的doctest.testmod()方法实现测试。
# 文档测试：>>> demo()；执行语句>>>符号后面一定要用空格；
# 文档测试：结果语句包含下一个>>>前的所有内容，不能空行。如3和'ab'前不能有空行；后面可以有空行；但不能有无关语句。


def func_demo(x, y):
    """ doc test demo
    >>> func_demo(1, 2)
    3
    >>> func_demo('a', 'b')
    'ab'
    >>> func_demo([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> func_demo({1:1}, {2:2})
    False
    >>> func_demo(1, '2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
    """
    if isinstance(a, dict):
        return False
    return x + y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
