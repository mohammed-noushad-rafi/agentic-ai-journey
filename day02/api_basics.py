import httpx
import json
response=httpx.get("https://api.github.com/users/mohammed-noushad-rafi")
print(response.status_code)
print(response.headers["content-type"])
data=response.json()
print(type(data))
print(data["login"])
print(data["public_repos"])
print(data["created_at"])
details={"latitude": 12.46,
    "longitude": 75.96,
    "current": "temperature_2m,wind_speed_10m"}
weather=httpx.get("https://api.open-meteo.com/v1/forecast" ,params=details)
print(weather.url)
data=weather.json()
print(json.dumps(data, indent=2))
temp = data["current"]["temperature_2m"]
unit = data["current_units"]["temperature_2m"]
print(f"Kushalnagar right now: {temp}{unit}")
def githubrepo(username):
    try:
        data=httpx.get(f"https://api.github.com/users/{username}",timeout=10)
        data.raise_for_status()
        return data.json()
    except httpx.HTTPStatusError as e:
        print(f"error {e.data.status_code}")
        return None
    except httpx.RequestError as e:
        print(f"error {e.data.status_code}")
        return None

respod=githubrepo("mohammed-noushad-rafi")    
print(respod)
payload={"role": "user", "content": "What is RAG"}
response=httpx.post("https://httpbin.org/post",json="payload",timeout=10)
print(response.status_code)
print(response.json()["json"])  

