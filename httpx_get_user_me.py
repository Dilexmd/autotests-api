import httpx

user_login_payload = {
    "email": "dlxmduser@example.com",
    "password": "111qqq"
}

user_login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=user_login_payload)
user_login_data = user_login_response.json()

access_token = user_login_data['token']['accessToken']
headers = {
    'Authorization':  f'Bearer {access_token}'
}

user_login_get = httpx.get('http://localhost:8000/api/v1/users/me', headers=headers)

print('User data:', user_login_data)
print('User response:', user_login_get)
print('Status code:', user_login_response.status_code)