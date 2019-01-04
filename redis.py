from redis import StrictRedis,ConnectionPool
redis=StrictRedis(host='localhost',port=6379,db=0,password='foobared')
redis.set('name','bob')
print(redis.get('name'))
pool=ConnectionPool(host='localhost',port=6379,db=0,password='foobared')
redis=StrictRedis(connection_pool=pool)
# redis://[:password]@host:port/db
# rediss://[:password]@host:port/db
# unix://[:password]@/path/to/socket.sock?db=db
url='redis://[:password]@host:port/db'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)
#常用操作
#键操作
#字符串操作
#列表操作
#集合操作
#有序集合操作
#散列操作
#redis-dump
#redis-load