
import asyncio

@asyncio.coroutine
def hello():
    print("Hello World")
    r = yield from asyncio.sleep(2)
    print("Hello Again")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
    
