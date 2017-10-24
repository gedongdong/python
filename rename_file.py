#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# form collections import Iterable
import os

def rename_file():
    file_list = os.listdir('/Users/gedongdong/prank')
    os.chdir('/Users/gedongdong/prank')
    for file_name in file_list:
        print "Old name is:"+file_name
        print "New name is:"+file_name.translate(None,'0123456789')
        os.rename(file_name,file_name.translate(None,'0123456789'))

rename_file()
