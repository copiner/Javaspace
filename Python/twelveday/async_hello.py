#python3.5.*
import threading
import asyncio

async def hello():
    print('Hello (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('World (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
