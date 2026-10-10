"""Call a public demo API with Python's built-in urllib."""
import json
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

def fetch_post(post_id=1):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    request = Request(url, headers={"User-Agent": "PythonLearningExample"})
    try:
        with urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            print("Post title:", data.get("title", "No title"))
            print("Post body:", data.get("body", "No body"))
    except HTTPError as error:
        print("HTTP error:", error.code)
    except URLError as error:
        print("Could not connect:", error.reason)
    except TimeoutError:
        print("The request timed out.")
    except json.JSONDecodeError:
        print("The server did not return valid JSON.")

if __name__ == "__main__":
    fetch_post(1)
    # This example needs an internet connection.
    # Practice: try another post ID and print userId.
