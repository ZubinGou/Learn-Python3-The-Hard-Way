#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 17:26:31
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
# 1
def make_inc(n):
    return lambda x: x + n

f = make_inc(98)
print(f(99))
print(f(0))

# 2
sum = lambda a, b, c: a + b + c
print(sum(23,23,1))

# 3
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda x: x[1])
print(pairs)
