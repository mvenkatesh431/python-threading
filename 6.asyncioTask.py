'''
Tasks:
Tasks within Asyncio are responsible for the execution of coroutines within an event loop. 
These tasks can only run in one event loop at one time and in order to achieve parallel execution you would have to run multiple event loops over multiple threads.

'''

import asyncio
import time

async def myTask():
    time.sleep(1)
    print("Processing Task")

async def main():
    #  generate 5 distinct tasks for our event loop to process.
    for i in range(5):
        # ensure_future creates the task.
        asyncio.ensure_future(myTask())
    pending = asyncio.all_tasks()
    # We can cancel a task using the `cancel()` function on `task`
    print(pending)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Completed All Tasks")
loop.close()


'''
Output:

>{<Task pending name='Task-4' coro=<myTask() running at asyncioTask.py:11>>, <Task pending name='Task-2' coro=<myTask() running at asyncioTask.py:11>>, <Task pending name='Task-1' coro=<main() running at asyncioTask.py:22> cb=[_run_until_complete_cb() at C:\Users\mvenk\AppData\Local\Programs\Python\Python310\lib\asyncio\base_events.py:184]>, <Task pending name='Task-3' coro=<myTask() running at asyncioTask.py:11>>, <Task pending name='Task-6' coro=<myTask() running at asyncioTask.py:11>>, <Task pending name='Task-5' coro=<myTask() running at asyncioTask.py:11>>}
Processing Task
Processing Task
Processing Task
Processing Task
Processing Task
Completed All Tasks
> 

'''