import asyncio
import time

from concurrent.futures import ThreadPoolExecutor


def get_url(url):
    print('start get url {}'.format(url))
    time.sleep(2)
    print('stop get url {}'.format(url))


def main():
    '''
    在协程中使用多线程的场景：
    协程中是不能加入阻塞IO的代码的，但是如果某个库或者接口只能提供阻塞的，需要放到线程中

    :return:
    '''
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    tasks = []
    for i in range(20):
        task = loop.run_in_executor(executor, get_url, 'g.cn'.format(i))
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)


if __name__ == '__main__':
    main()