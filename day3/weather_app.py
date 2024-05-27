import requests

weather_api_key = "9d00b3aa90d67f0feec63a21867cf141"

def main():
    lat, lon = get_coordinate()
    get_weather(lat,lon)

def get_weather(lat,lon):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            extract_weather_data(data)
        else:
            print("No data.")
            return None
    except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

def extract_weather_data(data):
    for weather_entry in data['list']:
        dt_txt = weather_entry['dt_txt']
        temp = weather_entry['main']['temp']
        description = weather_entry['weather'][0]['description']
        wind_speed = weather_entry['wind']['speed']
        print(f"At {dt_txt}, the temperature is {round(temp - 273,1)}°C with {description}. Wind speed: {wind_speed} m/s.")


def get_coordinate():
    city_name = "Tokyo"
    url=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={weather_api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            # 最初の結果の緯度経度を返す
            return data[0]['lat'], data[0]['lon']
        else:
            print("No data found for the city.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    main()