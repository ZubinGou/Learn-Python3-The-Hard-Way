#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 18:43:48
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os

num = "%e"% 1100
string = "%s" % "Hi there"
char = "%c" % 97

print(num, string, char, sep='\n')

x = 101
x //= 10
print(x)
x **= 2
print(x)

print(string.split)
print(string.split('e'))

class Thing(object):
    def test(self, message):
        print(self)
        print(message)

a = Thing()
a.test("Hell OP")

class Thing2(object):
    @staticmethod
    def test(arg):
        print(arg)

b = Thing2()
b.test("Well another way")
