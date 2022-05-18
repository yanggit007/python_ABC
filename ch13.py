# logging是python的一个内置模块(__init__.py)，logging文件夹下(config.py, handlers.py)的三个文件之一。
# logging有众多属性和方法，用来“制造”日志字符串，是打在屏幕上，还是以文件形式输出xx.log，都是用它的方法来实现的。
# logging可以通过getLogger()方法产生子体，类似从logging实例化。
# logging本身可以产生字符串，它的子体(logger)也可以产生字符串。
# logging拼凑出来的字符串：分5个级别，有约定的格式，自由输入只是其中的一项(message)。
# logging或logger的大概配置流程：先取名字，再分级别，然后是：输出方式，格式构成等等。（赋值前有默认值。）
# logging或logger可以用多种方法来配置：
#        1,通过中间商handler，用语句赋值；
#        2,通过吸入事先写好的xx.conf，xx.ini等文本文件。(用模块config.py里的fileConfig('log.conf')方法)
#        3,通过python字典
# logger直接出现在logging实例的后面时，格式会受影响。
#        如：logger的默认格式只有message,放在logging的实例之后，就会跟logging的实例格式一样。
# logging提供的字符串信息可以帮助人们了解程序的运行状况（日志作用）。

"""
debug(), info(), warning(), error(), critical()
https://docs.python.org/3/library/logging.html#logrecord-attributes
*** log.conf *** 通过事先准备好的文本文件赋值
"""

import logging

print(logging.BASIC_FORMAT)    # 可以看到它的默认格式

f = '%(asctime)s:%(filename)s:%(lineno)d:%(funcName)s:%(levelname)s:%(name)s:%(message)s'

# k = open('test.log', 'a')
logging.basicConfig(level='DEBUG', filename='logging_test.log', format=f, filemode='w')    # 配置logging

# logging本身各种准备之后的最终表演形式：
logging.debug('This is the logging debug.')
logging.info('This is the logging info.')
logging.warning('This is the logging warning.')
logging.error('This is the logging error.')
logging.critical('This is the logging critical.')


############################################################################
# “实例化”一个logger，并通过中间商handler来配置。

logger_1 = logging.getLogger(name='demo')                # 相当于实例化，还取了名字。（实例logger_1的名字是demo）
logger_1.setLevel(logging.DEBUG)                         # logger自己设置级别

# Create handlers 中间商
c_handler = logging.StreamHandler()                      # 中间商吸取“输出方式”(打在屏幕上)
f_handler = logging.FileHandler('logger_test.log', 'w')  # 中间商吸取“输出方式”(输出到文件)
c_handler.setLevel(logging.DEBUG)                        # 中间商吸取“级别设置”
f_handler.setLevel(logging.INFO)

# Create formatters and add it to handlers  格式通过另一个中介传到中间商
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)                         # 中间商吸取“格式”
f_handler.setFormatter(f_format)

# Add handlers to the logger  中间商把汇总的全部信息传给logger
logger_1.addHandler(c_handler)
logger_1.addHandler(f_handler)

# 实例化logger各种准备之后的最终表演形式：
logger_1.debug('this is logger_1 debug.')                # 执行结果：demo - DEBUG - this is logger_1 debug.
logger_1.info('this is logger_1 info.')                  # 执行结果：demo - INFO - this is logger_1 info.
logger_1.warning('this is logger_1 warning.')            # 执行结果：demo - WARNING - this is logger_1 warning.
logger_1.error('this is logger_1 error.')                # 执行结果：demo - ERROR - this is logger_1 error.
logger_1.critical('this is logger_1 critical.')          # 执行结果：demo - CRITICAL - this is logger_1 critical.


##########################################################################
# 通过事先准备好的文本文件赋值(pythonProject/log.conf)
#
# import logging
# from logging.config import fileConfig   # 很奇怪，直接import config用不了
# fileConfig('log.conf')                  # 通过fileConfig()方法直接吸入文本

# log.conf文件内容如下：
# [loggers]                               # logger的默认名字
# keys=root
#
# [handlers]                              # 中间商的输出方式
# keys=stream_handler
#
# [formatters]                            # 设置字符串格式句柄
# keys=formatter
#
# [logger_root]                           # logger的默认级别和输出方式
# level=DEBUG
# handlers=stream_handler
#
# [handler_stream_handler]                # 输出方式定义
# class=StreamHandler
# level=DEBUG
# formatter=formatter
# args=(sys.stderr,)
#
# [formatter_formatter]                   # 字符串默认格式
# format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s


##########################################################################
# 通python字典赋值方式没提
