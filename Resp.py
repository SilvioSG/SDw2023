import os
import requests  # Fazer chamadas de forma mais simples
import json
from user_ids import user_ids
from dotenv import load_dotenv

load_dotenv()

swd_url = os.getenv('URL')


def get_user(id):
    response = requests.get(f'{swd_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

def update_user(id):
    response = requests.put(f'{swd_url}/users/{id}')
    return True if response.status_code == 200 else None


users = [get_user(id) for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2, ensure_ascii=False))

for user in users:
    success = update_user(user)
    print(f'User {user["name"]} Update? {success}')
