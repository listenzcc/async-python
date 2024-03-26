"""
File: main.py
Author: Chuncheng Zhang
Date: 2024-03-15
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Practice for asynchronous operations in Python.
    The run_until_complete operation.

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-03-15 ------------------------
# Requirements and constants
import time
import random
import asyncio

from threading import Thread
from rich import print
from copy import deepcopy

from attrdict import AttrDict

global_tic = time.time_ns()

# %% ---- 2024-03-15 ------------------------
# Function and class


def ns2ms(ns: int) -> int:
    return int(ns*1e-6)


async def method(ad: AttrDict, sleep_secs: float = 0.1, copy: bool = False, failure_prob: float = 0.2) -> AttrDict:
    # Copy the input
    if copy:
        ad = deepcopy(ad)

    # Raise error randomly
    assert random.random() > failure_prob, f'Random error at p={failure_prob}'

    # Simulate time consuming operation
    tic = ns2ms(time.time_ns() - global_tic)
    value = ad.idx + 1
    time.sleep(sleep_secs)
    toc = ns2ms(time.time_ns() - global_tic)

    # Write back
    ad.update(dict(tic=tic, toc=toc, cost=toc-tic, value=value))
    return ad


# %% ---- 2024-03-15 ------------------------
# Play ground
if __name__ == '__main__':
    # ----------------------------------------
    # Single shot
    ad = AttrDict(idx=1)
    print(asyncio.run(method(ad, failure_prob=0.0)))

    # ----------------------------------------
    # Run until complete
    # 1. Get or create a new loop
    try:
        loop = asyncio.get_running_loop()
        print(f'Got running loop: {loop}')
    except RuntimeError:
        loop = asyncio.new_event_loop()
        print(f'Created loop: {loop}')
    asyncio.set_event_loop(loop)

    # 2. Create the jobs
    ads = [AttrDict(idx=i) for i in range(10)]
    jobs = asyncio.gather(*[method(ad) for ad in ads], return_exceptions=True)

    # 3. Run the jobs one-by-one until finished
    print(loop.run_until_complete(jobs))
    print(ads)


# %% ---- 2024-03-15 ------------------------
# Pending


# %% ---- 2024-03-15 ------------------------
# Pending
