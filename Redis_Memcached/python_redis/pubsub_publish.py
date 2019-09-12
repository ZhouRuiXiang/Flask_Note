# _*_ coding: utf-8 _*_
from redis import Redis

cache = Redis(host="10.70.223.101", port=6379, password="xcc86977")

for t in range(1):
    cache.publish("email", "1215686977@qq.com")

