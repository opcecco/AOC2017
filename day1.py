#!/usr/bin/env python

import sys

input = sys.argv[1]


# Part 1: Find sum of repeated digits (circular)

captcha = 0
for i in xrange(len(input)):
	if input[i] == input[(i + 1) % len(input)]:
		captcha += int(input[i])
		
print captcha


# Part 2: Find sum of digits that repeat halfway through the list

pad = len(input) / 2

captcha = 0
for i in xrange(len(input)):
	if input[i] == input[(i + pad) % len(input)]:
		captcha += int(input[i])
		
print captcha
