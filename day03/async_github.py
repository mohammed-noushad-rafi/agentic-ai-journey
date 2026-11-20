import asyncio
import time
import httpx

async def get_user(client, username):
    url = f"https://api.github.com/users/{username}"
    response = await client.get(url)
    if response.status_code != 200:
       raise Exception(f"User {username} not found")
    data = response.json()
    return (
    username,
    data["public_repos"],
    data["followers"]
    )

async def main():
    start_time = time.perf_counter()

    users = [
          "mohammed-noushad-rafi",
          "torvalds",
          "gvanrossum",
          "this_user_does_not_exist_12345"
        ]
       
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            *[get_user(client, username) for username in users],
            return_exceptions=True
        )
        for result in results:
            if isinstance(result, Exception):
                print(f"Error: {result}")
            else:
                username, repos, followers = result
                print(
                    f"User: {username} | "
                    f"Public Repos: {repos} | "
                    f"Followers: {followers}"
                )

    end_time = time.perf_counter()

    print(f"\nTotal time taken: {end_time - start_time:.2f} seconds")


asyncio.run(main())