# 进程池：进程数规定上限值，进程数达到上限值，新进程会等待，直到有进程结束；
# pool = multiprocessing.Pool(processes=3)
# pool type: <class 'multiprocessing.pool.Pool'>
#
# 线程池：线程数规定上限值，线程数达到上限值，新线程会等待，直到有线程结束；
# pool = multiprocessing.dummy.Pool(processes=3)
# pool type: <class 'multiprocessing.pool.ThreadPool'>
#
# map函数：是对.apply_async(f, args)方法的封装，用于调用同一函数的情况


import multiprocessing
import time


def process_func(process_id):
    print('process id %d start' % process_id)
    time.sleep(3)
    print('process id %d end' % process_id)


def main():

    pool = multiprocessing.Pool(processes=3)            # pool是一个类，处于run状态

    # pool.map(process_func, range(10))                 # 调用同一个函数的情况，才能用map函数
    for item in range(10):
        pool.apply_async(process_func, args=(item, ))   # .apply_async启动进程，阻塞for循环

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()


# import multiprocessing.dummy
# import time


# def process_func(process_id):
#     print('process id %d start' % process_id)
#     time.sleep(3)
#     print('process id %d end' % process_id)


# def main():

#     pool = multiprocessing.dummy.Pool(processes=3)

#     # pool.map(process_func, range(10))
#     for item in range(10):
#         pool.apply_async(process_func, args=(item, ))

#     pool.close()
#     pool.join()


# if __name__ == '__main__':
#     main()
