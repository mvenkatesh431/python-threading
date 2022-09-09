'''
Futures:
 Future objects are created with the intention that they will eventually be given a result some time in the future, 
 hence the name. This is beneficial as it means that within your Python program you can go off and perform other tasks whilst you are waiting for your Future to return a result.

 We can use the `ensure_future()` which takes `coroutine` and returns the `Future`
'''

import asyncio
from asyncio import tasks
from random import randint

async def processing(x):
    print(f"Starting Task {x}")
    delay = randint(1,10)
    await asyncio.sleep(delay)
    print(f"Task {x} took {delay} seconds to complete")

async def run():
    tasks = []
    for i in range(5):
        # Create future using `ensure_future`
        tasks.append(asyncio.ensure_future(processing(i)))

    # await these tasks completion using the await asyncio.gather() function
    await asyncio.gather(*tasks)


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.close()

if __name__ == "__main__":
    main()


'''
Output:
Starting Task 0
Starting Task 1
Starting Task 2
Starting Task 3
Starting Task 4
Task 2 took 2 seconds to complete
Task 0 took 6 seconds to complete
Task 4 took 6 seconds to complete
Task 3 took 6 seconds to complete
Task 1 took 9 seconds to complete
'''
