#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 15:33:15
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
def print_two(*args):
    arg1, arg2 = args;
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("zeddd", "shawww")

def print_all(f):
    print(f.read())

def rewind_f(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

cur_file = open('a.txt')
print_all(cur_file)
print("that's all.")
rewind_f(cur_file)

cur_line = 1
print_a_line(cur_line, cur_file)
print_a_line(cur_line+1, cur_file)


# print(3, [23 23 3])
