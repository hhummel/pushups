import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    total = time.perf_counter() - start
    print(f"{__file__} ran in {total} seconds")
