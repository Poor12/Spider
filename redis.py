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
#���ò���
#������
#�ַ�������
#�б����
#���ϲ���
#���򼯺ϲ���
#ɢ�в���
#redis-dump
#redis-load