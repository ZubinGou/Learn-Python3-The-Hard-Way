#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-20 17:04:47
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

print('Practice make prefect')
print('You\'d need to \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')
poem = '''
\t the lovely world
with logic so firmly planted
\n\twhere there is none.
'''

print("-------------")
print(poem)
print("-------------")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_points = 10000
beans, jars, crates = secret_formula(start_points)

print(f"with a starting point of: {start_points}")
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

start_points /= 10
print("we can also do that this way")
formula = secret_formula(start_points)
print('we\'d have {} beans, {} jars, and {} crates.'.format(*formula))
