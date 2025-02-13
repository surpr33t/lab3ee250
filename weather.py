import requests

# WeatherAPI key
WEATHER_API_KEY = 'f3dd73227ae94eb6aab214932251302'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    baseURL = "http://api.weatherapi.com/v1/current.json" 

    parameter = {  
        'key': WEATHER_API_KEY, 
        'q': city  
    }

    try: 
        # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
        request = requests.get(baseURL, params=parameter)  

        # TODO: Handle HTTP status codes:
        # - Check if the status code is 200 (OK), meaning the request was successful.
        # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
        if request.status_code == 200:
            data = request.json()  

            # TODO: Parse the JSON data returned by the API. Extract and process the following information:
            # - Current temperature in Fahrenheit
            tempF = data["current"]["temp_f"]  

            # - The "feels like" temperature
            tempFeel = data["current"]["feelslike_f"]  

            # - Weather condition (e.g., sunny, cloudy, rainy)
            condition = data["current"]["condition"]["text"]

            # - Humidity percentage
            humidity = data["current"]["humidity"]

            # - Wind speed and direction
            wind_speed = data["current"]["wind_mph"]
            wind_direction = data["current"]["wind_dir"]

            # - Atmospheric pressure in mb
            pressure_mb = data["current"]["pressure_mb"]

            # - UV Index value
            uvIndex = data["current"]["uv"]

            # - Cloud cover percentage
            cloudCover = data["current"]["cloud"]

            # - Visibility in miles
            visibility = data["current"]["vis_miles"]

            # TODO: Display the extracted weather information in a well-formatted manner.
            print(f"Weather data for {city}...")
            print(f"Temperature: {tempF}°F (Feels like {tempFeel}°F)")
            print(f"Condition: {condition}")
            print(f"Humidity: {humidity}%")
            print(f"Wind: {wind_speed} mph, Direction: {wind_direction}")
            print(f"Pressure: {pressure_mb} mb")
            print(f"UV Index: {uvIndex}")
            print(f"Cloud Cover: {cloudCover}%")
            print(f"Visibility: {visibility} miles\n")

        else:
            # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
            print(f"Error: {request.status_code}. Something went wrong.") 

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")  

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter a city name: ").strip()

    # TODO: Call the 'get_weather' function with the city name provided by the user.
    if city:
        get_weather(city)
    else:
        print("Error: Enter valid city.")

    pass
