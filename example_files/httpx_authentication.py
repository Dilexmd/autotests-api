import httpx


"""Login"""

login_payload = {
  "email": "dlxmduser@example.com",
  "password": "111qqq"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print('Login responce:', login_response_data)
print('Status code:', login_response.status_code)


"""Refresh"""

refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}

refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
refresh_response_data = refresh_response.json()

print('Refresh responce:', refresh_response_data)
print('Status code:', refresh_response.status_code)