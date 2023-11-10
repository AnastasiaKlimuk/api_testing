import requests  ##модуль который используют для упрощения работы с HTTP-запросами

def test_getting_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/users/5')
    print(r.status_code, r.json())