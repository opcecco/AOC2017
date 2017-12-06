#!/usr/bin/env python

"""
Advent of Code 2017: Day 5 Part 1
https://adventofcode.com/2017/day/5
"""

import sys

with open(sys.argv[1], 'r') as file:
	input = [int(line) for line in file.readlines()]
	
index = 0
count = 0

while index >= 0 and index < len(input):
	old_index = index
	index += input[index]
	input[old_index] += 1
	count += 1
	
print count
