import requests
import passwords

url = "http://localhost:80/basic-auth/russ/test"
response = requests.get(url, auth=(passwords.USERNAME, passwords.PASSWORD))

print(response.status_code, response.text)

