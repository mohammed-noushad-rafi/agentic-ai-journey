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