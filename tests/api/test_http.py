import pytest
import requests
import json
import sys

# Фікс друку для Windows
sys.stdout.reconfigure(encoding='utf-8')

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    print(json.dumps(r.json(), ensure_ascii=False, indent=2))
    assert r.status_code == 200
    assert headers['Server'] == 'github.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/defunkt/ola_kliuch')

    assert r.status_code == 404
    


