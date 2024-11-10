import requests
import json

def get_weather_data(city_name: str) -> str:
    # API key and base URL setup
    api_key = '677f8bbdf8e34cd0b1e95337240911'
    base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}'

    try:
        # Send the API request
        response = requests.get(base_url)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()

            # Retrieve necessary weather details
            location = data['location']['name']
            temperature = data['current']['temp_c']
            weather_condition = data['current']['condition']['text']

            # Return the weather details in a formatted JSON string
            return json.dumps({
                "location": location,
                "temperature": temperature,
                "weather_condition": weather_condition
            })

        else:
            # Return a message if the API call fails
            return json.dumps({
                "error": "Unable to fetch weather data",
                "status_code": response.status_code
            })

    except Exception as e:
        # Handle and return any exception encountered
        return json.dumps({
            "error": f"An error occurred: {str(e)}"
        })

if __name__ == "__main__":
    city_name = "New York"  
    print(get_weather_data(city_name))
