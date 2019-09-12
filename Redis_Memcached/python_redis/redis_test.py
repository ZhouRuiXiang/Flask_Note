# _*_ coding: utf-8 _*_
from redis import Redis

# ip:10.70.223.101
cache = Redis(host="10.70.223.101", port=6379, password="xcc86977")

# Redis 字符串操作
cache.set("username", "xingchen")
print(cache.get("username"))

# Redis list操作
cache.flushall()
print(cache.keys())
cache.lpush("name", "Mark")
cache.lpush("name", "Helen")
cache.lpush("name", "Tom")
cache.rpop("name")
print(cache.lrange("name", 0, -1))

# Redis set操作
cache.sadd("Fairy tales", "Green")
# cache.sadd("Fairy tales", "Andersen")
# cache.sadd("Fairy tales", "Aesop's Fables")
# cache.srem("Fairy tales", "Green")
# print(cache.smembers("Fairy tales"))
# print(cache.scard("Fairy tales"))

# Redis hash操作
cache.flushall()
cache.hmset("Media", {"Weibo": "sina", "paper": "newspaper"})
print(cache.hgetall("Media"))

# Redis transaction操作
cache.flushall()
pipeline = cache.pipeline()
pipeline.set("age", 19)
pipeline.set("sex", "male")
pipeline.execute()
print(cache.keys())

# Rediso pubsub操作
ps =cache.pubsub()
ps.subscribe("email")
while True:
    # ps.listen()返回的是一个迭代器
    for item in ps.listen():
        if item["type"] == "message":
            print(item.get("data"))
