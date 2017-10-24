#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib

def read_txt():
    files = open('/Users/gedongdong/movie_quotes/movie_quotes.txt')
    contents = files.read()
    files.close()
    check_result(contents)

def check_result(contents):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+contents)
    result = connection.read()
    print result
    connection.close()

read_txt()
