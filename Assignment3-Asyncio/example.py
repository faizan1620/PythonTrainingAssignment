# This file for demonstrating asyncio with sleep()

import time
import asyncio


async def function_1(delay):
    print(f"Function 1 started to execute will be taking {delay} seconds")
    print("Function 1 waiting for IO")
    await asyncio.sleep(delay)
    print("Function 1 completes its execution")


async def function_2(delay):
    print(f"Function 2 started to execute will be taking {delay} seconds")
    print("Function 2 waiting for IO")
    await asyncio.sleep(delay)
    print("Function 2 completes its execution")


async def function_3():
    print("In function 3")
    print("Function 3 completes its execution")


async def main():
    task1 = asyncio.create_task(function_1(12))

    task2 = asyncio.create_task(function_2(8))

    task3 = asyncio.create_task(function_3())

    print(f"started at {time.strftime('%X')}")

    # Wait until tasks are completed (should take
    # around max of all not sum of all time.)
    await task1
    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
