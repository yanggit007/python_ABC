# unittest单元测试：把要测试的python文件xx.py放在package包里，在上层目录中写测试文件test_xx.py
# 继承单元测试的TestCase类的步骤：先import unittest；之后class TestAdd(unittest.TestCase):；继承后，写自己的方法。
# 在方法中运用TestCase的assertEqual等方法进行测试。一个方法中可以有多个测试，这多个测试全通过才能算是一个通过。（即以方法数量计数）
# 执行测试的语句：unittest.main()放在if __name__ == '__main__':下面，避免python文件被调用时被执行。
# pycharm自动检测：只要有import unittest，pycharm的run '文件名'就会变成：run 'Python tests in 文件名'。所有>>>行都会高亮显示。
# VSCode和命令行不会自动检测，必须通过代码中的unittest.main()方法实现测试。
# 知识点：文件夹的右键弹出菜单中有：Make Directory as > Sources Root将当前路径作为源目录。有利于调用不同层级中的包。

import unittest
from demo.math import add


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 4), 5)

    def test_add_2(self):
        self.assertEqual(add(10, 20), 30)
        self.assertNotEqual(add(10, 20), 31)

    def test_add_3(self):
        self.assertRaises(ValueError, add, 1, 1.2)


if __name__ == '__main__':
    unittest.main()
