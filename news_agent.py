import requests
import json

def fetch_news(query: str, start_date: str, end_date: str, language: str = "en") -> str:
    # API endpoint and key configuration
    api_key = 'pub_587490b53d269d365ad2aba1ec4bf392f6277'
    api_url = f'https://newsdata.io/api/1/archive?apikey={api_key}&q={query}&language={language}&from_date={start_date}&to_date={end_date}'
    
    try:
        # Make the request to the API
        response = requests.get(api_url)
        
        # Check if the response is successful
        if response.status_code == 200:
            news_data = response.json()
            
            # Extract articles with necessary fields
            articles_list = [
                {
                    "title": article.get("title", "Title Not Available"),
                    "description": article.get("description", "Description Not Available"),
                    "published_date": article.get("pubDate", "Date Not Available")
                }
                for article in news_data.get("results", [])
            ]
            
            # Return the collected news articles in a formatted JSON string
            return json.dumps({"search_query": query, "articles": articles_list}, indent=2)
        
        else:
            # Return error information if the API call fails
            return json.dumps({"error": "Failed to retrieve news", "status_code": response.status_code})
    
    except Exception as error:
        # Handle any exceptions and return the error details
        return json.dumps({"error": f"Exception occurred: {str(error)}"})

if __name__ == "__main__":
    # Example usage with placeholders; replace with actual values
    example_query = "technology"
    example_start_date = "2023-11-01"
    example_end_date = "2023-11-10"
    print(fetch_news(example_query, example_start_date, example_end_date))
