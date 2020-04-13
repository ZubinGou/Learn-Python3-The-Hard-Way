#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 19:55:48
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

# ex39 dict
dic = {'adf':32, 'qew':54}
val = dic.get('ad')
print(val)
val2 = dic.get('fun', 'Does not exist!!!')
print(val2)

# ex40
import e40_mystuff as ms


ms.apple()
print(ms.tangerine)

# class
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!") # magic

thing = MyStuff()
thing.apple()
print(thing.tangerine)

'''
## 3 WAYS get things from things:
# dict
mystuff['apples']

# module
mystuff.apples()
print(myStuff.tangerine)

# class
thing = MyStuff()
thing.apples()
print(thing.tangerine)
'''

