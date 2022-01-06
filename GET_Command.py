# Create basic HTTP Client
import requests
response = requests.get("http://api.open-notify.org/astros.json")
# response = requests.get("http://www.booking.com/")
print(response)
print(response.json())