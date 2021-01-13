import requests

headers = {
        'Content-Type': 'application/json'
        }
requestResponse = requests.get("https://api.tiingo.com/api/test?token=4d109a21f529efe178e73aae6e710b8c24330e71",
                                    headers=headers)
print(requestResponse.json())