def my_sum(*args):
    result = 0
    for item in args:
        result += item
    return result


max_num = 100

print(my_sum(2, 5, 8, 13))  # 这种语句，只要执行文件import当前模块，就会被执行
if __name__ == '__main__':
    print(my_sum(2, 5, 8, 13))

# __name__是每个.py文件的默认属性名，无需定义，是一个字符串，当前文件值'__name__', 模块值是from后的路径文件名字符串
# import os
# print(dir(os))
# print(help(os.path)
