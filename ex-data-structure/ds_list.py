#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 17:38:20
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('kiwi'))
fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort(key=lambda x: x[-1])
print(fruits)

fruits.pop()
print(fruits)
fruits.pop(5)
print(fruits)

# using list as stacks
print()
stack = [3, 2, 5]
stack.append(6)
print(stack)
stack.pop()
print(stack)

# as queues
from collections import deque
queue = deque(['eric', 'john', 'michael'])
queue.append('Terry')
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)

# as queue also
queue = ['eric', 'john', 'michael']
queue.pop(0)
print(queue)

# list comprehensions
squares = list(map(lambda x:x**2, range(10)))
print(squares)

squares2 = [x**2 for x in range(10)]
print(squares2)

pairs = [(x, y) for x in range(100) for y in range(6,8) if x%y == 0]
print(pairs)

vec = [[1,2,3], [4,5,6], [7,8,9]]
nums = [num for elem in vec for num in elem]
print(nums)

from math import pi
pis = [str(round(pi, i)) for i in range(1, 6)]
print(pis)

# nested list comprehensions
mat = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     ]
mat_trans = [[row[i] for row in mat] for i in range(4)]
print(mat_trans)
mat_trans2 = list(zip(*mat))
print(mat_trans2)
