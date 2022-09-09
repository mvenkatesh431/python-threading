'''
AsyncIO event loop flavours:
- `run_until_complete` - Event loop run until the provided function finished execution.
        loop.run_until_complete(coRoutine())
- `run_forever()` - It will run the event loop forever (Until the stop method is called.)

'''

import asyncio

async def firstTask():
    # Long-Running task.
    while True:
        await asyncio.sleep(1)
        print(f"Running FirstTask")
    

async def secondTask():
    # Long-Running task.
    while True:
        await asyncio.sleep(1)
        print(f"Running SecondTask")

def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(firstTask())
        asyncio.ensure_future(secondTask())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

if __name__ == "__main__":
    main()


'''
Output:

Running FirstTask
Running SecondTask
Running FirstTask
Running SecondTask
Running FirstTask
Running SecondTask
Running FirstTask
Running SecondTask

'''