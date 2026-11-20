import asyncio
import time
import httpx

CITIES = {
    "Kushalnagar": (12.46, 75.96),
    "Madikeri": (12.42, 75.74),
    "Mysuru": (12.30, 76.64),
    "Bengaluru": (12.97, 77.59),
    "Mangaluru": (12.91, 74.86),
}

URL = "https://api.open-meteo.com/v1/forecast"


async def get_temp(client, city, lat, lon):
    params = {"latitude": lat, "longitude": lon, "current": "temperature_2m"}
    response = await client.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return city, data["current"]["temperature_2m"]


async def one_by_one():
    async with httpx.AsyncClient() as client:
        results = []
        for city, (lat, lon) in CITIES.items():
            results.append(await get_temp(client, city, lat, lon))
        return results


async def all_at_once():
    async with httpx.AsyncClient() as client:
        tasks = [get_temp(client, city, lat, lon) for city, (lat, lon) in CITIES.items()]
        return await asyncio.gather(*tasks)


async def main():
    start = time.time()
    print(await one_by_one())
    print(f"One by one: {time.time() - start:.2f}s")

    start = time.time()
    print(await all_at_once())
    print(f"All at once: {time.time() - start:.2f}s")

asyncio.run(main())
# import asyncio
# import time
# async def fetch_data(param):
#     print(f"do something with {param}")
#     await asyncio.sleep(param)
#     print(f"done wirh {param}")
#     return f"results of{param}"
# async def main():
#     task1=asyncio.create_task(fetch_data(1))
#     task2=asyncio.create_task(fetch_data(2))
#     result1=await task2
#     print("task 2 is completed")
#     result2=await task1
#     print("task1 is completed")
#     return [task1,task2]

# t1=time.perf_counter()
# results=asyncio.run(main())
# print(results)
# t2=time.perf_counter()
# print(f"finished in{t2-t1:.2f}seconds")