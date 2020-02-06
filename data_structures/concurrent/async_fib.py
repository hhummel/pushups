import asyncio

async def fib(n):
   if n <= 2:
       return 1
   else:
       return await fib(n- 1) + await fib(n - 2)

async def get_fib(n):
    result = await fib(n)
    print(f"get_fib({n}) = {result}")

async def main():
    await asyncio.gather(get_fib(33), get_fib(22), get_fib(11), get_fib(0))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Elapsed time: {elapsed} seconds")
