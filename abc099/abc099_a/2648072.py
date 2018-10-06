#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = raw_input()
num_input = int(input)
if num_input < 1000:
    input = '%03d' % num_input
    output = "ABC"
else:
    input ='%03d' % (num_input - 999)
    output = "ABD"

print output
