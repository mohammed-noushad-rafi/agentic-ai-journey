import asyncio
import time
import httpx

USERS = ["mohammed-noushad-rafi",
"torvalds",
"gvanrossum",
"this_user_does_not_exist_12345"
]

URL = "https://api.github.com/users/{username}"

async def get_user(client, username):
 url = URL.format(username=username)

 response = await client.get(url, timeout=10)
 if response.status_code != 200:
    raise Exception(f"User {username} not found")
 data = response.json()
 return (
    username,
    data["public_repos"],
    data["followers"]
    )

async def main():
 start = time.time()

 async with httpx.AsyncClient() as client:
    tasks = [
        get_user(client, username)
        for username in USERS
    ]
    results = await asyncio.gather(
        *tasks,
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
 print(f"\nTotal time taken: {time.time() - start:.2f}s")

asyncio.run(main())