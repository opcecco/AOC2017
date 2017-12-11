#!/usr/bin/env python

"""
Advent of Code 2017: Day 10 Part 1
https://adventofcode.com/2017/day/10
"""

import sys

# Return a sublist from our circular list
def get_circular_sublist(start, length):
	global circular_list
	sublist = []
	for i in xrange(start, start + length):
		sublist.append(circular_list[i % len(circular_list)])
	return sublist
	
	
# Set a section of our circular list to a given sublist
def set_circular_sublist(start, sublist):
	global circular_list
	for i in xrange(len(sublist)):
		circular_list[(i + start) % len(circular_list)] = sublist[i]
	return sublist
	
	
with open(sys.argv[1], 'r') as file:
	input = [int(num) for num in file.readline().split(',')]
	
# Initialize the circular list and positional values
circular_list = range(256)
current_position, skip_size = 0, 0

# Loop through input lengths, reverse sublists, and move cursor
for section_length in input:
	
	section = get_circular_sublist(current_position, section_length)
	set_circular_sublist(current_position, section[::-1])
	
	current_position += section_length + skip_size
	skip_size += 1
	
print circular_list[0] * circular_list[1]
