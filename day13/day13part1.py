#!/usr/bin/env python

"""
Advent of Code 2017: Day 13 Part 1
https://adventofcode.com/2017/day/13
"""

import sys

with open(sys.argv[1], 'r') as file:
	input_list = [[int(num) for num in line.split(': ')] for line in file.readlines()]
	
severity = 0

# Find which layers have movement patterns that do not evenly divide their layer number
for input in input_list:
	layer, length = input[0], input[1]
	if layer % (2 * (length - 1)) == 0:
		severity += layer * length
		
print severity
