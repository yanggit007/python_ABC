# 这个案例使用了实例化lock的.locked()方法，用来判断，等待所有线程结束。如60-62行
# lock = _thread.allocate_lock() 是ch20_6中thread_lock = threading.Lock()的本质

# 实例化锁lock的形式：
# <locked _thread.lock object at 0x105c9b8a0> | **.release()前后，两种状态
# <unlocked _thread.lock object at 0x105c9b8a0>

# lock实例化时是未锁状态；
# lock.acquire()方法之后锁定；lock.release()方法之后是未锁状态；
# lock.locked()方法用来判断锁的状态，返回bool值；

# _thread.start_new_thread(thread_function, (item,)) 线程实例化, 立即执行；
# _thread.allocate_lock() 锁实例化和线程实例化都是基于_thread模块，但锁与线程没有必然联系；

# threading.Thread(target=thread_function, args=(item, )) 线程实例化，不立即执行；
# threading.Lock() 锁实例化和线程实例化都是基于threading模块，锁与线程会有关联；

# 线程队列的初始化：tq = queue.Queue(maxsize=10) 基于queue模块，与threading模块无直接关联；
# 进程队列的初始化：pq = multiprocessing.Queue() 基于multiprocessing模块；
# 线程用的队列形式：自始至终是 <queue.Queue object at 0x1097179d0>
# 进程用的队列形式：自始至终是 <multiprocessing.queues.Queue object at 0x1064d0fd0>

# 队列的.put()方法：用于往队列里一个一个的放置信号（信号可以是任何数据类型，队列像列表，put像append）；
# 队列的.get()方法：用于阻塞，暂停程序，一次.get()方法必须提走一个信号，程序才能结束往下执行；

import time
import datetime
import _thread

date_time_format = '%H:%M:%S'


def get_time_str():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, date_time_format)


def thread_function(thread_id, lock):
    print('Thread %d\t start at %s' % (thread_id, get_time_str()))
    print('Thread %d\t sleeping' % thread_id)
    time.sleep(4)
    print('Thread %d\t finish at %s' % (thread_id, get_time_str()))
    lock.release()                        # 线程最后，解除当前线程锁，表示当前线程结束


def main():
    print('Main thread start at %s' % get_time_str())
    locks = []

    for item in range(5):                 # 实例化了5把锁，接着锁定，然后放在列表里
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    print(locks)

    for item in range(5):                 # 5次触发，每隔一秒触发，启动一个线程
        _thread.start_new_thread(thread_function, (item, locks[item]))
        time.sleep(1)
        print(locks)

    for item in range(5):                 # 判断5把锁是否都被解除，等待所有锁解除
        while locks[item].locked():
            time.sleep(1)
            print(locks)

    print('Main thread finish at %s' % get_time_str())


if __name__ == '__main__':
    main()
