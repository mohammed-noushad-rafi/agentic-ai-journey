import httpx
import json
def get_weather(latitude, longitude):
    #Calls Open-Meteo with timeout=10 and raise_for_status()  
    # Returns a dict like {"temperature": 24.1, "wind_speed": 6.3}
     # Returns None and prints a clear message if the request fails
    params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,wind_speed_10m",
}
    try:
        response=httpx.get("https://api.open-meteo.com/v1/forecast",params=params,timeout=10)
        response.raise_for_status()
        data=response.json()
        return {"temperature": data["current"]["temperature_2m"] ,"wind_speed": data["current"]["wind_speed_10m"],}
    except httpx.HTTPStatusError as e:
        print (f"error {e.response.status_code}")
        return None
    except httpx.RequestError as e:
        print (f"error{e}")
        return None
print(get_weather(12.46, 75.96))
   

