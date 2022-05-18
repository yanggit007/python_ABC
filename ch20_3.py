# threading.Thread类可把线程实例化后放在列表里，之后用.start()方法来启动线程。
# threading.Thread(target=thread_function, args=(item, )) 实例化线程，但不会启动线程。
# 实例化线程用.join()方法来延长主程序的结束时间，等待所有线程执行结束。如39-40行

import time
import datetime
import threading

date_time_format = '%H:%M:%S'


def get_time_str():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, date_time_format)


def thread_function(thread_id):
    print('Thread %d\t start at %s' % (thread_id, get_time_str()))
    print('Thread %d\t sleeping' % thread_id)
    time.sleep(4)
    print('Thread %d\t finish at %s' % (thread_id, get_time_str()))


def main():
    print('Main thread start at %s' % get_time_str())
    threads = []

    for item in range(5):                 # 实例化了5个线程放在列表里（创建线程）
        thread = threading.Thread(target=thread_function, args=(item, ))
        threads.append(thread)            # 类threading.Thread的对象自动管理线程锁

    print(threads)

    for item in range(5):                 # 5次触发，每隔一秒触发一个线程（启动线程）
        threads[item].start()             # 每个实例的start()方法
        time.sleep(1)
        print(threads)

    for item in range(5):                 # 等待所有线程执行结束
        threads[item].join()

    print(threads)

    print('Main thread finish at %s' % get_time_str())


if __name__ == '__main__':
    main()
