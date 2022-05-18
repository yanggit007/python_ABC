# 多线程，执行先后顺序混乱，不同步，不可预知；
# 这是一个线程混乱的例子，下个例子用互斥锁来解决；

import time
import threading


class MyThread(threading.Thread):
    def __init__(self, thread_id):
        super(MyThread, self).__init__()
        self.thread_id = thread_id
    
    def run(self):
        for item in range(10):
            print('Thread %d\t printing! time:%d' % (self.thread_id, item))

        time.sleep(1)
        
        for item in range(10):
            print('Thread %d\t printing! time:%d' % (self.thread_id, item))


def main():
    print('Main thread start')
    threads = []

    for item in range(5):                 # 实例化了5个线程放在列表里（创建线程）
        # thread = threading.Thread(target=thread_function, args=(item, ))
        thread = MyThread(item)
        threads.append(thread)            # 类threading.Thread的对象自动管理线程锁

    print(threads)

    for item in range(5):                 # 5次触发，每隔一秒触发一个线程（启动线程）
        threads[item].start()             # 每个实例的start()方法
        print(threads)

    for item in range(5):                 # 等待所有线程执行结束
        threads[item].join()

    print(threads)

    print('Main thread finish')


if __name__ == '__main__':
    main()
