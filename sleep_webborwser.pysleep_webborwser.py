#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# form collections import Iterable
import webbrowser
import time

print "wait..."+time.ctime()
i = 0
while i < 3:
    time.sleep(5)
    webbrowser.open('http://www.qq.com')
    i += 1
