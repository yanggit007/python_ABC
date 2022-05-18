# 一个工厂有很多车间，但在同一时段只允许一个车间运转，每个车间都有很多条作业线（场地，工人，设备和工具共同参与）；
# 单核CPU相当于一个工厂，进程相当于车间，线程就是作业线，一个车间里可能有多条作业线；
# 排队上厕所也算一条作业线，还有食堂线，工作线等等，多线程并行比单线程效率高，但可能会先后次序混乱；
#
# 本来原生线程完全由操作系统调度执行，但发牌照（lock）可帮助操作系统避免多线程杂乱无序，实现某种同步；
# 进程多般试图启动外部命令，线程则试图启动程序内部自定义的函数或方法；
# 多线程：硬件多线程|软件多线程；硬件多线程可实现真正的并行，软件多线程依靠的是快速切换；
# 
# 之前的学习都是单人单工作业系统，以下是单人多任务作业系统，像是很多条线在同时进行的感觉；
# _thread.start_new_thread(thread_function, (item,))

import time
import datetime
import _thread

date_time_format = '%H:%M:%S'            # 实时时间格式


def get_time_str():                      # 获取实时时间
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, date_time_format)


def thread_function(thread_id):          # 一个会执行4秒的线程
    print('Thread %d\t start at %s' % (thread_id, get_time_str()))
    print('Thread %d\t sleeping' % thread_id)
    time.sleep(4)
    print('Thread %d\t finish at %s' % (thread_id, get_time_str()))


def main():
    print('Main thread start at %s' % get_time_str())
    for item in range(5):                # 5个线程，每隔一秒启动一个
        # thread_function(item)
        _thread.start_new_thread(thread_function, (item,))
        time.sleep(1)
    time.sleep(6)                        # 手动等待所有线程结束
    print('Main thread finish at %s' % get_time_str())


if __name__ == '__main__':
    main()
