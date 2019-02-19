'''
高并发模式编程中具备的三个要素
事件循环 + 回调（驱动生成器） + IO多路复用（epoll）
asyncio是python用于解决异步io编程的一整套解决方案

tornado实现了web服务器（完成了socket编码，可以直接部署）
但是有一点需要特别需要注意的是，在使用数据库驱动的时候，不能使用平常使用到的传统的阻塞IO驱动

'''

import asyncio
import time

async def get_html(url):
    '''
    这是一个协程，需要注意的是协程必须要搭配事件循环一起使用
    :param url:
    :return:
    '''
    print('start get url')
    # 注意，这里不能简单地使用python自带的time.sleep()函数，因为python的sleep是同步阻塞的接口
    # 这样写的话，跟顺序写是同样的慢
    # time.sleep(2)
    # 这是一个耗时的操作，等待它执行完成需要加await
    # asyncio.sleep(2)
    # await后面必须跟的是一个awaitable的对象（协程就是awaitable的对象）
    # await time.sleep()
    # asyncio.sleep(2)
    print('stop get url')


def main():
    start_time = time.time()
    # loop可以理解为一个心脏，它不停地调度函数并执行，是单线程模式
    # 如果在协程中写了阻塞的代码，一个地方阻塞了，其他的代码都运行不了
    loop = asyncio.get_event_loop()
    tasks = [get_html('www.baidu.com') for i in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)


if __name__ == '__main__':
    main()