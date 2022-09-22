import requests

def test_get_token():
    url = "https://integrations.bynder-stage.com/v6/authentication/oauth2/token"

    payload = 'client_id=64368a3f-963e-45c0-b9d9-f8bac02a8815&client_secret=abf25d20-6243-4d40-ac98-a1b46421ad3f&grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)

def test_get_a_new_token():
    url = "https://integrations.bynder-stage.com/v6/authentication/oauth2/token"

    payload = 'client_id=64368a3f-963e-45c0-b9d9-f8bac02a8815&client_secret=abf25d20-6243-4d40-ac98-a1b46421ad3f&grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)