#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 12:05:03
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
from sys import argv

script, filename = argv

print(f"opening {filename}")

input("?")
target = open(filename,'w')
target.truncate()

print("give 3 lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("writing to file...")

target.write(line1+'\n'+line2+'\n'+line3+'\n')

print("closing...")
target.close()
