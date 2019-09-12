# -*- coding: utf-8 -*-#

"""
@Name:         main.py
@Description:  
@Author:       Mark
@Date:         2019\9\11 0011 16:18
"""
import memcache
mc = memcache.Client(["127.0.0.1:11211", "10.70.223.112"], debug=True)

mc.set('username', 'xingchen', time=120)
# print(mc.get('username'))
data = {
    'username': 'xingchen ',
    'password': '123456',
    'age': 20,
    'gender': 'male',
    'hometown': 'HubeiXiangyang'

}
mc.set('number', '111')
mc.set_multi(data)
mc.incr('number', delta=1)

print(mc.get('number'))
mc.delete('number')
print(mc.get('number'))