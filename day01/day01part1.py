#!/usr/bin/env python

"""
Advent of Code 2017: Day 1 Part 1
https://adventofcode.com/2017/day/1
"""

import sys

input = sys.argv[1]

captcha = 0

for i in xrange(len(input)):
	if input[i] == input[(i + 1) % len(input)]:
		captcha += int(input[i])
		
print captcha
