import requests
import json


def get_weather_forecast(city):
    api_key = "003be8e5969395fa2f7ac2eeaf2bc726"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful
        weathe_data = response.json()
        return weathe_data
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the weathe forecast:", e)
        return None

def display_weather_forecast(weather_data):
    if weather_data is not None:
        city = weathe_data["name"]
        temperature = weathe_data["main"]["temp"]
        description = weathe_data["weathe"][0]["description"]
        humidity = weathe_data["main"]["humidity"]

        print("Weathe forecast for", city)
        print("Temperature:", temperature, "°C")
        print("Description:", description)
        print("Humidity:", humidity, "%")
    else:
        print("No weathe forecast available.")

def main():
    city = input("Enter a city name: ")
    weathe_data = get_weathe_forecast(city)
    display_weathe_forecast(weathe_data)

if __name__ == "__main__":
    main()
