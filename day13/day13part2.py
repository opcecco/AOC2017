#!/usr/bin/env python

"""
Advent of Code 2017: Day 13 Part 2
https://adventofcode.com/2017/day/13
"""

import sys, itertools

with open(sys.argv[1], 'r') as file:
	input_list = [[int(num) for num in line.split(': ')] for line in file.readlines()]
	
success = False

# Increment a delay starting from 0
for delay in itertools.count(0):
	success = True
	
	# Determine if you can make it through
	for input in input_list:
		if (input[0] + delay) % (2 * (input[1] - 1)) == 0:
			success = False
			break
			
	if success:
		break
		
print delay
