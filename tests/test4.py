import requests  ##модуль который используют для упрощения работы с HTTP-запросами

def test_getting_posts():
    data = {
        'title': 'AnastasiyaTest',
        'body': 'just some text',
        'userId': 111
    }

    r = requests.post(url='https://jsonplaceholder.typicode.com/posts', data=data)
    print(r.status_code, r.json())