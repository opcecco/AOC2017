#!/usr/bin/env python

"""
Advent of Code 2017: Day 1 Part 2
https://adventofcode.com/2017/day/1
"""

import sys

input = sys.argv[1]

pad = len(input) / 2
captcha = 0

for i in xrange(len(input)):
	if input[i] == input[(i + pad) % len(input)]:
		captcha += int(input[i])
		
print captcha
