#!/usr/bin/env python

"""
Advent of Code 2017: Day 10 Part 2
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
	input = [ord(num) for num in file.readline().strip()]
	
# Initialize the circular list, lengths vector, and positional values
input += [17, 31, 73, 47, 23]
circular_list = range(256)
current_position, skip_size = 0, 0

# Loop through input lengths, reverse sublists, and move cursor for 64 rounds
for round in xrange(64):
	for section_length in input:
		
		section = get_circular_sublist(current_position, section_length)
		set_circular_sublist(current_position, section[::-1])
		
		current_position += section_length + skip_size
		skip_size += 1
		
dense_hash = ''

# Calculate the dense hash by XORing blocks of 16 bytes
for block_start in xrange(0, 256, 16):
	block_value = 0
	
	for i in xrange(block_start, block_start + 16):
		block_value ^= circular_list[i]
		
	dense_hash += '%02x' % block_value
	
print dense_hash
