import requests

response = requests.get('https://dekkov.pythonanywhere.com/send-email/"tranhoan"')
print(response.status_code)
print(response.json())