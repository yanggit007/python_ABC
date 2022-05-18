# 任何一个进程，启动时，会有一个返回值；结束时，也会有一个返回值；
# 返回值类型：可能是整数，也可能是一个类；
# 父进程依靠返回值知道子进程的状态，决定分配资源还是销毁资源；
# 父进程默认不会判断子进程的状态，这是产生僵尸进程和孤儿进程的原因； 
# 
# 孤儿进程：指父进程已退出，子进程没有退出；孤儿进程会被1号进程(init进程)收养；
# 僵尸进程：指父进程没退出，子进程退出了，父进程没有调用函数获取子进程的状态，没有收回子进程占用的资源；
# 1号init进程：会周期性调用wait函数来清除各个僵尸子进程；
# wait函数原理：首先进程调用wait，然后阻塞自己，开始寻找僵尸子进程，阻塞到找到为止，找到后，销毁子进程后返回；
# 
# 创建进程的方式：（***调用外部命令的方式也可以调用程序自身***）
# 调用外部命令的方式：rt = os.system("dir") | rt = os.execvp("") 启动返回值rt是整数；
# 调用外部命令的方式：rt = subprocess.call(['cmd line']) | rt = subprocess.check_call(['cmd line']) 启动返回值rt是整数；
# 调用外部命令的方式：rtc = subprocess.Popen('cmd line') 构造返回值rtc是类，程序不会立即启动，类有.start()方法；
# 调用程序自身的方式：rtc = multiprocessing.Process() | rtc = multiprocessing.Process(function, args) 构造返回值同上行；
# 对比调用多线程方式：rtc = threading.Tread() | rtc = threading.Tread(function, args) 构造同上行，但类不含pid，不存在僵孤；
# 复制现有主进程Mac：pid = os.fork() 返回值是整数；
# 总结：返回值是整数时，子进程都立即执行，不用监管子进程是否结束；
#      返回值是类时，子进程不会立即执行，执行后需要监管子进程是否结束；
#
# 监管子进程结束的方式: 1, 阻塞，等待子进程结束的返回值 rtc.wait() | rtc.waitpid()
#                    2, 阻塞，主动扫描子进程是否结束 rtc[i].join()
#                    3, Queue队列护航
#
# 实例化进程的形式：
# <Popen: returncode: None args: 'ping -c 2 www.baidu.com'> | **.wait()前后，两种状态
# <Popen: returncode: 0 args: 'ping -c 2 www.baidu.com'>
# 
# <Process name='Process-1' parent=1024 initial> | **.start()前后
# <Process name='Process-1' pid=1026 parent=1024 started> | **.join()前后
# <Process name='Process-1' pid=1026 parent=1024 stopped exitcode=0>
# 
# <MyProcess name='MyProcess-1' parent=1038 initial> | **.start()前后
# <MyProcess name='MyProcess-1' pid=1040 parent=1038 started> | **.join()前后
# <MyProcess name='MyProcess-1' pid=1040 parent=1038 stopped exitcode=0>
# 
# 进程队列的初始化：pq = multiprocessing.Queue()
# 进程用的队列形式：自始至终是 <multiprocessing.queues.Queue object at 0x1064d0fd0>
#
#
# 实例化线程的形式：
# <Thread(Thread-1, initial)>
# <Thread(Thread-1, started 123145394872320)>
# <Thread(Thread-1, stopped 123145394872320)>
# 
# <MyThread(Thread-1, initial)>
# <MyThread(Thread-1, started 123145454747648)>
# <MyThread(Thread-1, stopped 123145454747648)>
# 
# 线程队列的初始化：tq = queue.Queue(maxsize=10)
# 线程用的队列形式：自始至终是 <queue.Queue object at 0x1097179d0>
# 
# 队列的.put()方法：用于往队列里一个一个的放置信号（信号可以是任何数据类型，队列像列表，put像append）；
# 队列的.get()方法：用于阻塞，暂停程序，一次.get()方法必须提走一个信号，程序才能结束往下执行；


# import os
# import subprocess
#
# if os.name == 'nt':
#     return_code = subprocess.call(['cmd', '/C', 'dir'])
# else:
#     return_code = subprocess.call(['ls', '-l'])
#
# if return_code == 0:
#     print('Run success!')
# else:
#     print('Something wrong!')


# import os
# import subprocess
#
# try:
#     if os.name == 'nt':
#         subprocess.check_call(['cmd', '/C', 'test command'])
#     else:
#         subprocess.check_call(['ls', 'test command'])
#
# except subprocess.CalledProcessError as e:
#     print('Something wrong!', e)


# import os
# import subprocess

# if os.name == 'nt':
#     ping = subprocess.Popen('ping -n 5 www.baidu.com', shell=True, stdout=subprocess.PIPE)

# else:
#     ping = subprocess.Popen('ping -c 2 www.baidu.com', shell=True, stdout=subprocess.PIPE)

# ping.wait()

# print(ping.pid)

# print(ping.returncode)

# output = ping.stdout.read()
# print(output)


# from multiprocessing import Process
# import os


# def info(title):
#     print(title)
#     print('module name:\t', __name__)
#     print('parent process:\t', os.getppid())
#     print('process id:\t', os.getpid())


# def f(name):
#     info('function f')
#     print('hello', name)


# if __name__ == '__main__':
#     print('Current ID: %d\t Shell ID: %d' % (os.getpid(), os.getppid()))
#     info('main line')
#     p = Process(target=f, args=('PYTHON', ))
#     p.start()
#     p.join()


# from multiprocessing import Process
# import os


# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()
    
#     def run(self):
#         print('module name:\t', __name__)
#         print('parent process:\t', os.getppid())
#         print('process id:\t', os.getpid())


# def main():
#     processes = []

#     for item in range(5):
#         processes.append(MyProcess())

#     for item in range(5):
#         processes[item].start()

#     for item in range(5):
#         processes[item].join()


# if __name__ == '__main__':
#     main()


from multiprocessing import Process, Queue
import os

result_queue = Queue()


class MyProcess(Process):
    def __init__(self, q):
        super(MyProcess, self).__init__()
        self.q = q

    def run(self):
        output = 'module name %s\t' % __name__
        output += 'parent process: %d\t' % os.getppid()
        output += 'process id: %d' % os.getpid()
        self.q.put(output)             # 每开一个进程，顺道加一个队列字段


def main():
    processes = []
    for item in range(5):
        processes.append(MyProcess(result_queue))  # 把队列绑在进程实例化上

    for item in range(5):
        processes[item].start()       # 进程一启动，在进程中给队列加字段

    for item in range(5):
        processes[item].join()        # 等待进程结束时，队列字段数就是进程数

    while not result_queue.empty():   # 取空了循环才会结束
        result = result_queue.get()   # 通过打印的字段数就知道执行过多少个进程
        print(result)


if __name__ == '__main__':
    main()
