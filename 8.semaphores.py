'''
These semaphores have an internal counter that is incremented and decremented whenever either an acquire or a release call is made.
'''

import asyncio
from random import randint

async def processing(mySemaphore, x):
    print(f"Starting Task {x}")

    await mySemaphore.acquire()
    print(f"Task {x} - Aquired Semaphore - Inside the Critical Section")
    delay = randint(1,10)
    await asyncio.sleep(delay)
    print(f"Task {x} - Took {delay} seconds to complete")
    print(f"Task {x} - Releasing Semaphore ")
    mySemaphore.release()

async def run():
    mySemaphore = asyncio.Semaphore(value=3)
    tasks = []
    for i in range(5):
        # Create future using `ensure_future`
        tasks.append(asyncio.ensure_future(processing(mySemaphore, i)))

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

Threads-in-Python>  python .\8.semaphores.py
Starting Task 0
Task 0 - Aquired Semaphore - Inside the Critical Section
Starting Task 1
Task 1 - Aquired Semaphore - Inside the Critical Section
Starting Task 2
Task 2 - Aquired Semaphore - Inside the Critical Section
Starting Task 3
Starting Task 4
Task 0 - Took 5 seconds to complete
Task 0 - Releasing Semaphore 
Task 3 - Aquired Semaphore - Inside the Critical Section
Task 1 - Took 7 seconds to complete
Task 1 - Releasing Semaphore 
Task 4 - Aquired Semaphore - Inside the Critical Section
Task 2 - Took 9 seconds to complete
Task 2 - Releasing Semaphore 
Task 4 - Took 2 seconds to complete
Task 4 - Releasing Semaphore 
Task 3 - Took 7 seconds to complete
Task 3 - Releasing Semaphore 
Threads-in-Python> 
'''