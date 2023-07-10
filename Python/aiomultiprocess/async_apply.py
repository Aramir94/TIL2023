import asyncio
import random

import aiomultiprocess


async def coro_func(value: int) -> int:
    await asyncio.sleep(random.randint(1, 3))
    return value * 2


async def main():
    tasks = []
    async with aiomultiprocess.Pool() as pool:
        tasks.append(pool.apply(coro_func, (1,)))
        tasks.append(pool.apply(coro_func, (2,)))
        tasks.append(pool.apply(coro_func, (3,)))

        results = await asyncio.gather(*tasks)
        print(results)  # Output: [2, 4, 6]


if __name__ == "__main__":
    asyncio.run(main())