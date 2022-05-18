# thread_lock = threading.Lock() | thread_lock.acquire() | thread_lock.release()
# 本质上是_thread.allocate_lock() | thread_lock是实例化对象，实例化有三个重要方法。(.locked())
# threding.Lock相当于为多线程设置绿色通道规则，对没参入规则的线程没有限制；
# 对参入规则的线程，在同一时间只能有一个线程在运行，实现线程同步。没规则线程可乱入；
# .acquire()语句与.release()语句之间的线程，就是参入规则的线程。如20-23行；

import time
import threading

thread_lock = None


class MyThread(threading.Thread):
    def __init__(self, thread_id):
        super(MyThread, self).__init__()
        self.thread_id = thread_id
    
    def run(self):

        thread_lock.acquire()
        for item in range(3):
            print('Thread %d\t printing! time:%d' % (self.thread_id, item))
        thread_lock.release()

        time.sleep(1)
        
        thread_lock.acquire()
        for item in range(3):
            print('Thread %d\t printing! time:%d' % (self.thread_id, item))
        thread_lock.release()


def main():
    print('Main thread start')
    threads = []

    for item in range(5):                 # 实例化了5个线程放在列表里（创建线程）
        # thread = threading.Thread(target=thread_function, args=(item, ))
        thread = MyThread(item)
        threads.append(thread)            # 类threading.Thread的对象自动管理线程锁

    print(threads)

    for item in range(5):                 # 5次触发，每隔一秒触发一个线程（启动线程）
        threads[item].start()             # 每个实例的.start()方法
        
        thread_lock.acquire()
        print(threads)
        thread_lock.release()

    for item in range(5):                 # 等待所有线程执行结束
        threads[item].join()

    print(threads)

    print('Main thread finish')


if __name__ == '__main__':
    thread_lock = threading.Lock()
    main()
