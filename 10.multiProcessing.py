'''
When to Use:
MultiThreading - Use for I/O Bound Tasks, Ex: Reading, Writing from files, reading/writing via network, db, etc.
MultiProcessing - Use for CPU Bound Tasks, Ex: Image processing, video transcode, streaming, etc.
'''


from time import perf_counter
from multiprocessing import Process

def processing():
    # CPU Intensive Task
    num = 1
    while num<=300000000:
        num += 1


if __name__ == "__main__":
    sTime = perf_counter()

    # With-out Multiprocessing
    # processing()
    # processing()

    # With Multi-Processing
    p1 = Process(target=processing)
    p2 = Process(target=processing)

    # To Create mutliple processes, 
    # processes = [multiprocessing.Process(target=processing, args=[filename]) 
    #                       for filename in filenames]

    # Start Processes
    p1.start()
    p2.start()

    # Join Processes
    p1.join()
    p2.join()

    eTime = perf_counter()

    print(f"Time Took {eTime - sTime} seconds")


'''
Without MultiProcessing:
> python .\10.multiProcessing.py
Time Took 16.56388309993781 seconds
>

With MultiProcessing:
> python .\10.multiProcessing.py
Time Took 10.059609099989757 seconds
> 

'''