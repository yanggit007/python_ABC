# os.system('ls') 创建ls进程，相当于在终端直接运行ls，调用外部命令是最简单创建进程的方式；
# os.fork() 创建当前进程的子进程，返回值是0，
# os.getpid()获取当前进程的ID，os.getppid()获取当前进程的父进程ID
#
# 启动终端，操作系统就会创建一个新的进程；
# 新建一个shell窗口，操作系统就会新建一个子进程，这就是python主进程的父进程；
# python主进程的父进程ID，可以在稍后进入python3.9后用os.getppid()看到；
# 在shell窗口启动python3.9, 操作系统就会新建下一级的子进程，这才是python程序的主进程；
#
# python程序每次执行时，操作系统就会创建一个新的主进程ID，但shell的进程ID变不变取决于是否重启shell。
# 也就是：python主进程ID会在每次执行代码时更换，主进程的父进程ID会在重启shell时更换；
# 在主进程里创建的任何进程都是子进程；
# 每个进程都有一个不重复的“进程ID号”，或称“pid”，process identify;
# 在shell里：ps -ef 可查看进程ID；如同在windows里查看任务管理器；
#
# 在一个进程里可以通过调用os.fork(), 要求操作系统新建一个子进程；
# 通过os.fork()函数新建的子进程，本质上与父进程完全相同，两个进程唯一的区别就是fork的返回值。
# 子进程返回值为0，父进程接收子进程的pid作为返回值；
# 调用os.fork()函数后，相当于分岔成两个一样的进程，之后两个进程并发执行同一个程序；
# 子进程可以用execve()程序，或者if语句改道执行其它语段，子进程完成时会返回SIGCHLD量；
# 默认主进程并不管子进程是否执行完成，随时会中断程序，但主进程的.wait()函数可以等待子进程的完成信号；
# 父进程和子进程：既并发执行，又相互独立；也就是说，它们是“异步执行”，“异步结束”的；
# 父进程和子进程在内存上：是完全不同的两个空间地址，子进程的空间是父进程分配的，父进程可以销毁那个空间。


import os
import sys
 
processName = 'parent'
 
print("Program pid: %d\t processName: %s\t Shell id: %d" % (os.getpid(), processName, os.getppid()))
print('\n')
 
# attempt to fork child process
try:
    forkPid = os.fork()
except OSError:
    sys.exit("Unable to create new process.")     # ***** 打印字符串后，退出>>> 模式 *****
 
# Am I parent process?
if forkPid != 0:
    print("Parent pid: %d\t processName: %s\t forkPid: %d" % (os.getpid(), processName, forkPid))
 
# Am I child process?
elif forkPid == 0:
    processName = "child"
    print("Children pid: %d\t processName: %s\t forkPid: %d" % (os.getpid(), processName, forkPid))

print("Finish pid: %d\t processName: %s" % (os.getpid(), processName))
print('\n')


# import os

# print('MainProcess ID: %d\t Shell ID: %d' % (os.getpid(), os.getppid()))

# if os.name == 'nt':
#     return_code = os.system('dir')
# else:
#     return_code = os.system('ls')

# print('MainProcess ID: %d\t Shell ID: %d' % (os.getpid(), os.getppid()))

# if return_code == 0:
#     print('Run success!')
# else:
#     print('Something wrong!')

# print('MainProcess ID: %d\t Shell ID: %d' % (os.getpid(), os.getppid()))


# import os

# print('MainProcess ID: %d\t Shell ID: %d' % (os.getpid(), os.getppid()))
# print('\n')

# pid = os.fork()

# print('Current ID: %d\t Upper ID: %d' % (os.getpid(), os.getppid()))

# if pid == 0:
#     print('子 ChildProcess, my ID: %s.' % os.getpid())
#     print('\n')

# else:
#     print('父 Created a %s ChildProcess.' % (pid, ))
#     print('\n')


# import os

# pid = os.fork()  # fork反复拷贝，fork英文是分岔的意思

# if pid == 0: 
#     print("子",os.getpid(), os.getppid()) 

# else: 
#     print("父",os.getpid(), os.getppid()) 
