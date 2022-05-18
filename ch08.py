import os
from sys import path, version, platform
import math
import random
import demo.my_math                           # 执行结果：28
from my_math import max_num                   # 执行结果：18

print(os.getcwd())
print(path)  # if '/Users/Jet/PycharmProjects/pythonProject' not in sys.path: \n sys.path.append('')
print(version)
print(platform)                               # 执行结果：darwin
print(demo.my_math.max_num)                   # 这种自建模块调用属性，需要路径写全
print(max_num)

print(math.pi)                                # 执行结果：3.141592653589793
print(math.e)                                 # 执行结果：2.718281828459045
print(math.ceil(2.1))                         # 执行结果：3                  浮点数往上取整
print(math.floor(2.1))                        # 执行结果：2                  浮点数往下取整
print(math.pow(5, 3))                         # 执行结果：125                5的3次方
print(math.log(100, 10))                      # 执行结果：2.0                求对数
print(math.sqrt(144))                         # 执行结果：12.0               求平方根
print(math.sin(math.pi/2))                    # 执行结果：1.0                求三角函数值
print(math.degrees(math.pi))                  # 执行结果：180.0              弧度转度数
print(math.radians(180))                      # 执行结果：3.141592653589793  度数转弧度

print(random.random())                        # 执行结果：0.2507821095466517 随机取0-1间浮点数
print(random.uniform(1, 150))                 # 执行结果：68.90131932817404  随机取浮点数
print(random.randint(1, 150))                 # 执行结果：15                 随机取整数
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(l1))                      # 执行结果：7                  随机抽取
random.shuffle(l1)                            # 打乱顺序
print(l1)                                     # 执行结果：[1, 6, 2, 7, 5, 3, 4, 8]

print(abs(7 - 12))                            # 执行结果：5                  取绝对值

# 创建虚拟环境：相当于生成一套简装版配置文件，解释器（mac的解释器采取调用，win是复制一份）
# 通过pycharm创建虚拟环境：File - New Project - Create Project对话框
# Win: python -m venv xxx | Mac: python3.9 -m venv xxx 命令行创建虚似环境，其中的venv是必须的。
# 虚拟环境的文件夹名称由用户定，但文件夹内的文件系统有严格的位置和名称，由系统默认，包括解释器。
# 第三方插件只要选定了解释器，就相当于选择好了安装位置和适用范围。

# Win: venv/Scripts/activate.bat | Mac: source bin/activate  命令行进入(venv)环境
# activate -- 激活的意思  |  它内部代码的本质是：集体修改程序的各种路径，实现从一个环境变到另一环境
# 不进入(venv）环境，没有pip命令。注：(venv)环境不是>>>环境。
# 不进入(venv)环境，主程序下安装包格式：python3.9 -m pip install packagename
# (venv)环境下，命令行：pip list第三方模块列表； pip install flask安装第三方模块
# (venv)环境下键入python3.9，进入>>> 模式就可以import第三方模块了
# (venv)环境下安装第三方模块才会在虚拟环境中，（第三方模块可以安装到虚拟环境中，也可以安装到全局中。）

### (venv)环境下 pip常规操作 ###
# pip install SomePackage          # 安装最新版本
# pip install SomePackage==1.0.4   # 安装指定版本
# pip uninstall SomePackage        # 删除某个包
# pip list                         # 显示所有安装的包
# pip list --outdated              # 显示所有可更新的包，并显示最新版本
# pip show sphinx                  # 显示包的详细信息
# pip search peppercorn            # 从PyPi搜索包

# activate                         # 进入虚拟环境 （本质就是把各种路径批量换成新环境的路径）
# deactivate                       # 退出虚拟环境 （本质就是把各种路径再批量改回去）

# import模块：1，内置模块； 2，第三方模块； 3，自建模块
# import …… 形式：只能import模块文件(去掉.py)，内置和第三方模块不用路径，自建模块需要路径
# import …… 调用时的样子（sys.path, demo.my_math.max_num, 自建模块需要路径)

# from ….….… import a 形式：前面是路径和模块文件（不要.py），后面是模块中的属性或方法（不要()）
# from ….….… import a, b, c 形式：后面可以跟多个方法和属性，不要()
# from ….….… import *  不建议这种整个调法，容易覆盖现有相同代码，import sys也是整个调，但可以不覆盖现有代码，除非有执行

# 模块在import时，其中的print等都会被执行，之后调用时，只会执行调用语句。
# 模块文件中在if __name__ == '__main__': 语句下用print()等语句测试，调用时不会被执行。
# __name__在当前python文件中出现，默认值是字符串："__main__"
# __name__在python模块文件中出现，默认值是字符串："~.~.~.xx.py" (模块文件的路径和名称)

# python中不支持 “直接带点” 或者 “以数字开头” 的文件作为模块文件导入。
# python中模块的文件名命名规则和变量命名规则相同。

# python的包package文件夹内：标准情况应该有__init__.py空文件；没有的话，可能有的IDE可以运行，有的IDE不可以运行；

# Mac终端命令行常用命令：pwd, ls, cd ..
# Win提示命令行常用命令：path, dir, cd..

# pypi.org网站：python package index上有各种link，库资源
