#!/usr/bin/env python

"""
Advent of Code 2017: Day 2 Part 1
https://adventofcode.com/2017/day/2
"""

import sys

with open(sys.argv[1], 'r') as file:
	input = [[int(num) for num in row.split()] for row in file.readlines()]
	
checksum = sum([max(row) - min(row) for row in input])
print checksum
