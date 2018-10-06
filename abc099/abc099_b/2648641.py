#!/usr/bin/env python
# -*- coding: utf-8 -*-

a,b =map(int, raw_input().split(' '))

n = b - a

sum = (n * n + n) / 2

output = sum - b

print output
