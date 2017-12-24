#!/usr/bin/env python

"""
Advent of Code 2017: Day 15 Part 1
https://adventofcode.com/2017/day/15
"""

import sys

generator_a, generator_b = int(sys.argv[1]), int(sys.argv[2])

count = 0

for i in xrange(40000000):
	generator_a = (generator_a * 16807) % 2147483647
	generator_b = (generator_b * 48271) % 2147483647
	
	if generator_a & 0xFFFF == generator_b & 0xFFFF:
		count += 1
		
print count
