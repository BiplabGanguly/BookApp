import requests

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = 'AIzaSyDyaNw7QjVwiAiwGNDE3kNqAjHtLcofhWQ'  # Replace with your actual API key

def fetch_books(query, max_results=10):
    try:
        response = requests.get(GOOGLE_BOOKS_API_URL, params={
            'q': query,
            'key': API_KEY
        })
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON data if request is successful
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        # Handle HTTP errors (e.g., 404, 500)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        # Handle other requests-related errors (e.g., network issues)
    except Exception as err:
        print(f"An error occurred: {err}")
        # Handle any other exceptions
    return None  # Return None or an empty dictionary if an error occurs