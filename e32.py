#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 17:42:06
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
the_count = list(range(1, 6))
print(the_count)
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
    print(f"this is count {num}")

for fruit in fruits:
    print(f"A fruits of type: {fruit}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

