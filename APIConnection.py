import requests
import json


api_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
# Specify API Key, and Application ID specific to your application
API_KEY = your_api_key
APPLICATION_ID = your_application_id
headers = {
    "x-app-key": API_KEY,
    "x-app-id": APPLICATION_ID,
    "Content-Type": "application/json"

}
food = input("What food would you like to find? ")
body = {
    "query": food
}
response = requests.post(api_url, headers = headers, json= body)
if response.status_code == 200:
    data = response.json()

    print(str(data["foods"][0]["nf_calories"]) + " calories in a serving size of " +
      str(data["foods"][0]["serving_qty"]))
else:
    print("Food not found")
