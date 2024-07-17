import requests

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

def get_weather(location):
    """
    Fetches weather data from the API for the specified location.
    Args:
        location (str): City name or coordinates (e.g., "Seattle" or "47.6062,-122.3321").
    Returns:
        dict: Weather data (temperature, conditions, humidity, wind speed).
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric",  # Use metric units (Celsius)
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_info = {
                "temperature": data["main"]["temp"],
                "conditions": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }
            return weather_info
        else:
            print(f"Error fetching weather data: {data.get('message', 'Unknown error')}")
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
    return None

def display_weather(weather_data):
    """
    Displays weather information to the user.
    Args:
        weather_data (dict): Weather data returned by get_weather().
    """
    if weather_data:
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Conditions: {weather_data['conditions']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    user_location = input("Enter a city name or coordinates (e.g., Seattle or 47.6062,-122.3321): ")
    weather_data = get_weather(user_location)
    display_weather(weather_data)
