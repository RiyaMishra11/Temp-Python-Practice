# Day 6 - 22: API and JSON Practice
import json
from urllib.parse import urlencode
from urllib.request import Request

# 1. Convert dictionary to JSON
def dict_to_json():
    data = {"name": "Aman", "age": 21, "city": "Delhi"}
    print(json.dumps(data, indent=4))

# 2. Convert JSON to dictionary
def json_to_dict():
    data = json.loads('{"name":"Riya","marks":92}')
    print(data)

# 3. Save JSON to a file
def save_json():
    data = {"course": "Python", "students": ["Aman", "Riya", "Karan"]}
    with open("course_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# 4. Read JSON from a file
def read_json():
    try:
        with open("course_data.json", encoding="utf-8") as f:
            print(json.load(f))
    except FileNotFoundError:
        print("Run save_json() first.")

# 5. Update a JSON-style dictionary
def update_data():
    data = {"name": "Aman", "score": 80}
    data["score"] = 95
    data["passed"] = True
    print(data)

# 6. Build URL query parameters
def build_query():
    params = {"city": "Delhi", "limit": 10, "active": True}
    print(urlencode(params))

# 7. Create an HTTP GET request
def get_request():
    request = Request("https://example.com/api",
                      headers={"Accept": "application/json"})
    print(request.method, request.full_url)

# 8. Create an HTTP POST request
def post_request():
    payload = json.dumps({"name": "Aman", "score": 90}).encode()
    request = Request("https://example.com/api", data=payload,
                      headers={"Content-Type": "application/json"},
                      method="POST")
    print(request.method, payload.decode())

# 9. Validate required API fields
def validate_response(data):
    required = ["id", "name", "email"]
    missing = [key for key in required if key not in data]
    print("Missing:", missing if missing else "None")

# 10. Parse API-style records
def parse_records():
    text = '[{"id":1,"name":"Aman","score":88},{"id":2,"name":"Riya","score":94}]'
    for item in json.loads(text):
        print(f"{item['id']}: {item['name']} - {item['score']}")

if __name__ == "__main__":
    dict_to_json()
    json_to_dict()
    build_query()
    get_request()
    post_request()
    validate_response({"id": 1, "name": "Aman", "email": "a@example.com"})
    parse_records()
