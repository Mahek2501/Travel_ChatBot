import json
import ollama
import asyncio
from weather_agent import get_weather
from itinerary_agent import get_tourist_places
from news_agent import get_news

# Function to retrieve antonyms for specific words
def fetch_antonyms(word: str) -> str:
    antonyms_dict = {
        "hot": "cold",
        "small": "big",
        "weak": "strong",
        "light": "dark",
        "lighten": "darken",
        "dark": "bright",
    }
    return json.dumps(antonyms_dict.get(word, "Antonym not found in the dictionary"))

# Function to simulate fetching flight schedules (in a real-world scenario, this might be an API call)
def fetch_flight_schedule(departure: str, arrival: str) -> str:
    flight_data = {
        "NYC-LAX": {"departure": "08:00 AM", "arrival": "11:30 AM", "duration": "5h 30m"},
        "LAX-NYC": {"departure": "02:00 PM", "arrival": "10:30 PM", "duration": "5h 30m"},
        "LHR-JFK": {"departure": "10:00 AM", "arrival": "01:00 PM", "duration": "8h 00m"},
    }
    flight_key = f"{departure}-{arrival}".upper()
    return json.dumps(flight_data.get(flight_key, {"error": "Flight not available"}))

async def execute_interaction(model: str, user_input: str):
    client = ollama.AsyncClient()

    # Initial user message
    messages = [{"role": "user", "content": user_input}]

    # Primary API call to handle user's query
    response = await client.chat(
        model=model,
        messages=messages,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "fetch_flight_schedule",
                    "description": "Retrieve flight schedule between two locations",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "departure": {"type": "string", "description": "Starting city"},
                            "arrival": {"type": "string", "description": "Destination city"},
                        },
                        "required": ["departure", "arrival"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Fetch current weather for a specified city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "City name"},
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_news",
                    "description": "Fetch the latest news for a given city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "City name"},
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_itinerary",
                    "description": "Retrieve popular tourist attractions for a specific city",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {"type": "string", "description": "City name"},
                        },
                        "required": ["city"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "fetch_antonyms",
                    "description": "Retrieve antonyms for a specified word",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "word": {"type": "string", "description": "Word to find antonyms for"},
                        },
                        "required": ["word"],
                    },
                },
            },
        ],
    )

    # Process model's response
    messages.append(response["message"])

    # If the model response doesn’t involve a tool call, print the response and end
    if not response["message"].get("tool_calls"):
        print("Model Response:", response["message"]["content"])
        return

    # Define available functions for handling tool calls and execute them if necessary
    available_functions = {
        "fetch_flight_schedule": fetch_flight_schedule,
        "fetch_antonyms": fetch_antonyms,
        "get_weather": get_weather,
        "get_itinerary": get_tourist_places,
        "get_news": get_news,
    }

    for tool in response["message"]["tool_calls"]:
        func = available_functions.get(tool["function"]["name"])
        if func:
            args = tool["function"]["arguments"]
            function_result = func(**args)
            print(f"{tool['function']['name']} Result:", function_result)

# Main interaction loop for user input
if __name__ == "__main__":
    while True:
        user_input = input("Please enter your question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        asyncio.run(execute_interaction("llama3.2:1b", user_input))

