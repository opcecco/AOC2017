#!/usr/bin/env python

"""
Advent of Code 2017: Day 15 Part 2
https://adventofcode.com/2017/day/15
"""

import sys

generator_a, generator_b = int(sys.argv[1]), int(sys.argv[2])

count = 0

# Loop through generators 5 million times and count how many match their lower 16 bits
for i in xrange(5000000):
	
	while True:
		generator_a = (generator_a * 16807) % 2147483647
		if generator_a % 4 == 0:
			break
			
	while True:
		generator_b = (generator_b * 48271) % 2147483647
		if generator_b % 8 == 0:
			break
			
	if generator_a & 0xFFFF == generator_b & 0xFFFF:
		count += 1
		
print count
