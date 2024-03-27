import redis
import random

def get_random_quote():
    db_r = redis.Redis(host='localhost', port=6379, db=0)
    size = int(db_r.get('size'))
    # print('size:', size)
    return db_r.get(random.randint(0, size))



