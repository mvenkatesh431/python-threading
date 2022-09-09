'''
Race Condition:
A Race Condition occurs when multiple concurrent workers try to modify a shared variable, array etc. concurrently 
and they start to produce erroneous results due to timing issues. We can use sync primitives like Lock to overcome race conditions.
'''

import asyncio
from random import randint

async def processing(lock, x):
    print(f"Starting Task {x}")

    async with lock:
        print(f"Task {x} - Locked - Inside the Critical Section")
        delay = randint(1,5)
        await asyncio.sleep(delay)
        print(f"Task {x} - Took {delay} seconds to complete")
    print(f"Task {x} - UnLocked ")    

async def run():
    lock = asyncio.Lock()
    tasks = []
    for i in range(5):
        # Create future using `ensure_future`
        tasks.append(asyncio.ensure_future(processing(lock, i)))

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


Threads-in-Python> python .\asyncioLocks.py
Starting Task 0
Task 0 - Locked - Inside the Critical Section
Starting Task 1
Starting Task 2
Starting Task 3
Starting Task 4
Task 0 - Took 1 seconds to complete
Task 0 - UnLocked 
Task 1 - Locked - Inside the Critical Section
Task 1 - Took 5 seconds to complete
Task 1 - UnLocked 
Task 2 - Locked - Inside the Critical Section
Task 2 - Took 1 seconds to complete
Task 2 - UnLocked 
Task 3 - Locked - Inside the Critical Section
Task 3 - Took 4 seconds to complete
Task 3 - UnLocked 
Task 4 - Locked - Inside the Critical Section
Task 4 - Took 1 seconds to complete
Task 4 - UnLocked 
Threads-in-Python> 
'''