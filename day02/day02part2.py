#!/usr/bin/env python

"""
Advent of Code 2017: Day 2 Part 2
https://adventofcode.com/2017/day/2
"""

import sys

with open(sys.argv[1], 'r') as file:
	input = [[int(num) for num in row.split()] for row in file.readlines()]
	
checksum = 0

for row in input:
	for i in xrange(len(row)):
		
		num = row[i]
		divisors = row[:i] + row[i + 1:]
		
		for d in divisors:
			if num % d == 0:
				checksum += num / d
				
print checksum
