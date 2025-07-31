import requests

# Paste your OpenWeatherMap API key below
API_KEY = "0018a6cd74ac9349287f43875ce3debc"

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            print("Error:", data.get("message", "Unknown error"))
            return None

    except requests.RequestException as e:
        print(" Network Error:", e)
        return None

def display_weather(info):
    print("\n Weather Info:")
    print(f"City: {info['city']}")
    print(f"Temperature: {info['temperature']}°C")
    print(f"Condition: {info['weather'].capitalize()}")
    print(f"Humidity: {info['humidity']}%")
    print(f"Wind Speed: {info['wind_speed']} m/s\n")

def main():
    print("== Weather App ==")
    city = input("Enter city name: ")
    data = get_weather(city)
    if data:
        display_weather(data)
    else:
        print(" Could not get weather data.")

if __name__ == "__main__":
    main()
