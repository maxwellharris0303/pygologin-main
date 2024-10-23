import os
from dotenv import load_dotenv
import json
import requests
import random

load_dotenv()

# Access the environment variables
TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")

def add_proxy(profile_id):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }

    proxy_session_id = random.randbytes(10).hex()

    data = {
        "autoProxyRegion": "us",
        "host": "brd.superproxy.io",
        "mode": "http",
        "password": "b6wj9r5p2wqi",
        "port": 22225,
        "torProxyRegion": "us",
        "username": f"brd-customer-hl_541e29d0-zone-residential_proxy1-session-{proxy_session_id}"
    }

    url = f'{BASE_URL}browser/{profile_id}/proxy'


    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 204:
        return proxy_session_id
    else:
        return "Failed"