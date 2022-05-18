# 队列就是时序控制器，让程序按照队列的要求进行。
# 若把队列放在for循环中，队列等待时，for循环会一起等待，起暂停作用。
# 如第39行：队列在等下一组数据时，for循环就会暂停等待
# Queue队列的get()方法：在队列(容器)为空时会一直等待，暂停，直到有数据进入。
# 标准库queue模块提供多种队列：Queue | LifoQueue | PriorityQueue

import time
import threading
import queue

work_queue = queue.Queue(maxsize=10)
result_queue = queue.Queue(maxsize=10)


class WorkerThread(threading.Thread):
    def __init__(self, thread_id):
        super(WorkerThread, self).__init__()
        self.thread_id = thread_id
    
    def run(self):
        while not work_queue.empty():
            work = work_queue.get()
            time.sleep(3)
            out = 'Thread %d\t received %s' % (self.thread_id, work)
            result_queue.put(out)


def main():
    print('Main thread start')

    for item in range(10):
        work_queue.put('message id %d' % item)

    for item in range(2):
        thread = WorkerThread(item)
        thread.start()

    for item in range(10):            # 本质上是自动调用threading.lock
        result = result_queue.get()   # 多个线程可以共用同一个Queue实例，阻塞for循环
        print(result)

    print('Main thread finish')


if __name__ == '__main__':
    main()
