import json

import requests

# Send a GET request
url = "http://127.0.0.1:8000"
r = requests.get(url)


print("Status Code:", r.status_code)


# Print the welcome message if the response contains JSON data
try:
    data = r.json()
    if "message" in data:
        print("Welcome Message:", data["message"])
except json.JSONDecodeError:
    print("Response does not contain JSON data.")



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send a POST request
url = "http://127.0.0.1:8000"
r = requests.post(url, json=data)


# Print the status code
print("Status Code:", r.status_code)
# Print the result if the response contains JSON data
try:
    result_data = r.json()
    print("Result:", result_data)
except json.JSONDecodeError:
    print("Response does not contain JSON data.")
