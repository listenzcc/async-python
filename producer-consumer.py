"""
File: producer-consumer.py
Author: Chuncheng Zhang
Date: 2024-03-26
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Async example of producer and consumer operations

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-03-26 ------------------------
# Requirements and constants
import time
import asyncio

from threading import Thread


# %% ---- 2024-03-26 ------------------------
# Function and class


async def consumer(queue: asyncio.Queue):
    print(f'---- Consumer starts')
    i = 0
    # Run forever
    while True:
        time.sleep(0.5)
        item = await queue.get()
        queue.task_done()
        # Break if get the None
        if item is None:
            break
        print(f'    {i:4d} | Consumer got: {item} | {queue.qsize()}')
        i += 1
    print(f'---- Consumer finished')


async def producer(queue: asyncio.Queue):
    for _ in range(1000):
        await asyncio.sleep(0.1)
        inp = input('>> ')
        if inp == 'q':
            break
        await queue.put(inp)

    await queue.put(None)


def _producer(queue: asyncio.Queue):
    for _ in range(1000):
        inp = input('>> ')
        if inp == 'q':
            break
        queue.put_nowait(inp)
    queue.put_nowait(None)


async def main():
    queue = asyncio.Queue()  # type: asyncio.Queue
    for j in range(10):
        queue.put_nowait(j)
    # Run the consumer in background
    _ = asyncio.create_task(consumer(queue))
    # Run the producer blocking the system
    Thread(target=_producer, args=(queue, )).start()
    # Wait for the queue._unfinished_tasks back to zero
    await queue.join()


# %% ---- 2024-03-26 ------------------------
# Play ground
if __name__ == '__main__':
    asyncio.run(main())

    print('All done.')


# %% ---- 2024-03-26 ------------------------
# Pending


# %% ---- 2024-03-26 ------------------------
# Pending
