import redis
def add_quote(quote):
    db_r = redis.Redis(host='localhost',port=6379,db=0)
    size = int(db_r.get('size'))
    size += 1
    db_r.set('size', size)
    db_r.set(size, quote)



