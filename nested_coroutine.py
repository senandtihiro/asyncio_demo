
import asyncio
import time


async def get_html(sleep_times):
    print('waiting')
    await asyncio.sleep(sleep_times)
    print('done after {} s'.format(sleep_times))


def main():
    task1 = get_html(1)
    task2 = get_html(2)
    task3 = get_html(3)
    tasks = [task1, task2, task3]
    loop = asyncio.get_event_loop()

    # 对任务的取消功能
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print('cancel task')
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()


if __name__ == '__main__':
    main()