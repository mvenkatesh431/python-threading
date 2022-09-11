
'''
Asyncio requires the event loop. The event loop schedules and handles the `asyncio.coroutines`

Coroutines:
coroutines are essentially lightweight versions of your more traditional threads. 
By using these we essentially enable ourselves to write asynchronous programs 
that are very similar to threads but they run on top of a single thread

We can create coroutines using `async` keyword or `@asyncio.coroutine` decorator.

To create and pause a coroutine, you use the Python async and await keywords:
- The async keyword creates coroutine.
- The await keyword pauses a coroutine.

To run a coroutine, you need to execute it on an event loop. or use the asyncio.run function

'''

import asyncio
from random import randint


async def myCoroutine(input):
    print(f"Processing {input}")
    await asyncio.sleep(input)


def main():
    # Create the event loop
    loop = asyncio.get_event_loop()

    # Assign work to event loop and wait until the assinged tasks are finished.
    loop.run_until_complete(myCoroutine(randint(1,10)))

    # close the event_loop
    loop.close()

main()