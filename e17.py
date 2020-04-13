#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 15:28:58
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

import os
from sys import argv
from os.path import exists

in_file = open('b.txt')
indata = in_file.read()

out_file = open('a', 'w')
out_file.write(indata)

out_file.close()
in_file.close()
