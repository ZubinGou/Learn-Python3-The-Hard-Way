#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 20:15:29
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
# del statement
a = list(range(10))
print(a)
del a[2]
print(a)
del a[:]
print(a)

# tuples and sequences
t = 1233, 243543, 'welle'
print(type(t))
print(t)
u = t, (34, 34)
print(u)
v = t, 34, 33
print(v)
w = ((23,4324), [342,'sdf'])
print(w)
print(type(w[1]))

singleton = 'hell'
print(len(singleton))
# see, magic
singleton = 'hell',
print(len(singleton))

t = 434,'343','bd'
a, b, c = t
print(b,a)
