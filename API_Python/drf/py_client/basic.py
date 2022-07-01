
import requests

# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/"  # "http://127.0.0.1:8000/"


get_reponse = requests.get(endpoint)
print(get_reponse.text)
# print(get_reponse.json())
print(get_reponse.status_code)
