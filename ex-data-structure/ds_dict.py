#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 20:28:36
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
tel = {'jack': 4098, 'sape': 4139}

del tel['sape']
tel['riv'] = 3247
tel['amy'] = 1243
print(tel)
print(list(tel))
print(sorted(tel))
print(list(tel.values()))

square = {x: x**3 for x in range(1, 10, 2)}
print(square)

dic =  dict(jack=32.234, guido=93.2, robin=99)
print(dic)

# looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i, v, sep=': ')

for i in range(9, 0, -2):
    print(i, end=', ')
print()
for i in reversed(range(1, 10, 2)):
    print(i, end=', ')
print()

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filter_data = [v for v in raw_data if not math.isnan(v)]
print(filter_data)
print()

# more magic on coditions
a = 4; b = 9; c = 9
print(a < b == c)
str1, str2, str3 = '14.', '25345', 'dsfj'
non_null = str1 or str2 and str3
print(non_null)
print('C' < 'Java' < 'Pascal' < 'Php' < 'Python')
print((1,2,3) == (1.0, 2.0, 3.0))
