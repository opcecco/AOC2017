#!/usr/bin/env python

"""
Advent of Code 2017: Day 14 Part 1
https://adventofcode.com/2017/day/14
"""

import sys

# Calcualte the knot-hash for a string, using a given formatter
def knot_hash(string):
	data = [ord(character) for character in string] + [17, 31, 73, 47, 23]
	circular_list = range(256)
	current_position, skip_size = 0, 0
	
	# Loop through input lengths, reverse sublists, and move cursor for 64 rounds
	for round in xrange(64):
		for section_length in data:
			
			for i in xrange(current_position, current_position + (section_length // 2)):
				j = 2 * current_position + section_length - i - 1
				circular_list[i % 256], circular_list[j % 256] = circular_list[j % 256], circular_list[i % 256]
				
			current_position += section_length + skip_size
			skip_size += 1
			
	dense_hash = 0
	
	# Calculate the dense hash by XORing blocks of 16 bytes
	for block_start in xrange(0, 256, 16):
		block_value = reduce(lambda a, b: a ^ b, circular_list[block_start:block_start + 16])
		dense_hash <<= 8
		dense_hash += block_value
		
	return dense_hash
	
	
input = sys.argv[1]

# Count all binary digits in all hashes
total = 0
for row in xrange(128):
	hash = knot_hash('%s-%d' % (input, row))
	while hash != 0:
		hash &= hash - 1
		total += 1
		
print total
