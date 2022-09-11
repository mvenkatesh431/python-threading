'''
ProcessPoolExecutor is similar to the ThreadPoolExecutor.
'''

import time
from random import randint
from concurrent.futures import ProcessPoolExecutor


def processing(id, cnt):
    num = 0
    print(f"Processing Task {id}...")
    # Similate CPU Bound task
    while num <= cnt:
        num += 1
    print(f"Task {id} is Completed")


if __name__ == "__main__":

    sTime = time.perf_counter()

    with ProcessPoolExecutor(max_workers=2) as pool:
        print("assigning work")
        # we can use the `submit` function to assign the work to the pool of Processes.
        pool.submit(processing, 1, randint(50000000, 1000000000))
        pool.submit(processing, 2, randint(50000000, 1000000000))
        pool.submit(processing, 3, randint(50000000, 1000000000))
        
        # we can even use the `map` function 
        # pool.map(processing, tasks)
    
    eTime = time.perf_counter()

    print(f"Took {eTime-sTime} seconds to finish")


'''
Output:
> python .\11.ProcessPools.py 
assigning work
Processing Task 1...
Processing Task 2...
Task 1 is Completed
Processing Task 3...
Task 2 is Completed
Task 3 is Completed
Took 39.191284499829635 seconds to finish
> 

Note: It only started two processes as we kept the `max_workers=2`
'''

    

