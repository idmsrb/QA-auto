import asyncio
import time
async def fun1(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('Функция збс')

async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('Ещё збс')

async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2

print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))