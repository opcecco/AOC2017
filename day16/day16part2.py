#!/usr/bin/env python

"""
Advent of Code 2017: Day 16 Part 1
https://adventofcode.com/2017/day/16
"""

import sys

with open(sys.argv[1], 'r') as file:
	input_list = file.readline().split(',')
	
original_dancers = list('abcdefghijklmnop')
dancers = original_dancers[:]

# Loop through all input moves
for input in input_list:
	
	# Spin
	if input[0] == 's':
		for i in xrange(int(input[1:])):
			dancers.insert(0, dancers.pop())
			
	# Exchange
	if input[0] == 'x':
		position1, position2 = (int(pos) for pos in input[1:].split('/'))
		dancers[position1], dancers[position2] = dancers[position2], dancers[position1]
		
	# Partner
	if input[0] == 'p':
		position1, position2 = (dancers.index(val) for val in input[1:].split('/'))
		dancers[position1], dancers[position2] = dancers[position2], dancers[position1]
		
# Get reordering
reordering = [original_dancers.index(program) for program in dancers]
print ''.join(dancers)

dancers = [dancers[index] for index in reordering]
print ''.join(dancers)