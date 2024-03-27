import redis
import requests

def init_database():
    db_r = redis.Redis(host='localhost', port=6379, db=0)
    response = requests.get('https://dummyjson.com/quotes')
    data = response.json()
    quotes = data['quotes']
    db_r.set('size', len(quotes))

    for quote in quotes:
        id = quote['id']
        content = quote['quote']
        db_r.set(id, content)





