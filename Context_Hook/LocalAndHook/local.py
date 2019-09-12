# -*- coding: utf-8 -*-#

# Name:         local.py
# Description:  
# Author:       Mark
# Date:         2019\8\27 0027 10:56
from threading import Thread
from werkzeug.local import Local

local = Local()
local.request = "abc"

local.request
class MyThread(Thread):
    def run(self):
        # global request
        local.request = "cba"
        print("子线程：", local.request)


mythread = MyThread()
mythread.start()
mythread.join()

# 主线程
print("主线程：", local.request)



