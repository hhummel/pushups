import asyncio

from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

async def fib(n):
   if n <= 2:
       return 1
   else:
       return await fib(n- 1) + await fib(n - 2)

def sync_fib(n):
    if n <= 2:
        return 1
    else:
        return sync_fib(n - 1) + sync_fib(n - 2)

async def get_fib(n):
    result = await fib(n)
    print(f"get_fib({n}) = {result}")
    return n, result

def sync_get_fib(n):
    result = sync_fib(n)
    print(f"get_fib({n}) = {result}")
    return n, result

async def main():
    data = await asyncio.gather(get_fib(33), get_fib(32), get_fib(31), get_fib(30), get_fib(33), get_fib(32), get_fib(31), get_fib(30))
    return data

if __name__ == "__main__":
    import time
    print("asyncio:")
    s = time.perf_counter()
    data = asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Elapsed time: {elapsed} seconds")
    print("Data: ", data)

    p = ThreadPool(6)
    print("thread pool:")
    s = time.perf_counter()
    data = p.map(sync_get_fib, [33, 32, 31, 30]*4)
    elapsed = time.perf_counter() - s
    print(f"Elapsed time: {elapsed} seconds")
    print("Data: ", data)

    p = Pool(6)
    print("multiprocessing:")
    s = time.perf_counter()
    data = p.map(sync_get_fib, [33, 32, 31, 30]*20)
    elapsed = time.perf_counter() - s
    print(f"Elapsed time: {elapsed} seconds")
    print("Data: ", data)
