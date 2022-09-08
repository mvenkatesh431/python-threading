'''
ThreadPoolExecutor helps us to create mutliple threads and do the tasks in concurrent fashion.
It will work very effective for the I/O Bound tasks.

ThreadPoolExecutor we can effectively mitigate this bottleneck by doing multiple fetches concurrently and processing each page as it returns
'''

# Create ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from random import randint
import threading


def process(x):
    print(f"Processing Input {x}, Thread {threading.current_thread()}")

# Thread pool with max workers as 4. Pool will have at max 4 concurrent threads
# tPool = ThreadPoolExecutor(max_workers=4)
# # we can use the `submit` function to assign the work to the pool of threads.
# tPool.submit(process, (randint(5, 100)))
# tPool.submit(process, (randint(5, 100)))
# tPool.submit(process, (randint(5, 100)))


def main():
    # Another way : By using the ContextManager
    with ThreadPoolExecutor(max_workers=4) as tPool:
        # we can use the `submit` function to assign the work to the pool of threads.
        tPool.submit(process, (randint(5, 100)))
        tPool.submit(process, (randint(5, 100)))
        tPool.submit(process, (randint(5, 100)))

if __name__ == '__main__':
    main()


'''
Output:
$ python threadPools.py
Processing Input 22, Thread <Thread(ThreadPoolExecutor-0_0, started 37844)>
Processing Input 57, Thread <Thread(ThreadPoolExecutor-0_0, started 37844)>
Processing Input 91, Thread <Thread(ThreadPoolExecutor-0_1, started 47144)>
$
'''

