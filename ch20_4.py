# 用自定义的子类MyThread继承threading.Thread类，并把线程放进子类自动运行的的run方法里；
# 实例化线程时就不用再传是哪个线程了，只传线程需要的参数即可，适合线程相同的情况；
# 之后同样是用.start()方法启动，用.join()方法在主程序中等待所有线程结束。
# 在构造函数中继承父类构造函数：super(MyThread, self).__init__()

import time
import datetime
import threading

date_time_format = '%H:%M:%S'


def get_time_str():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, date_time_format)


class MyThread(threading.Thread):
    def __init__(self, thread_id):
        super(MyThread, self).__init__()
        self.thread_id = thread_id
    
    def run(self):
        print('Thread %d\t start at %s' % (self.thread_id, get_time_str()))
        print('Thread %d\t sleeping' % self.thread_id)
        time.sleep(4)
        print('Thread %d\t finish at %s' % (self.thread_id, get_time_str()))


def main():
    print('Main thread start at %s' % get_time_str())
    threads = []

    for item in range(5):                 # 实例化了5个线程放在列表里（创建线程）
        # thread = threading.Thread(target=thread_function, args=(item, ))
        thread = MyThread(item)
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
