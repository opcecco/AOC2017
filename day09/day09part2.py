#!/usr/bin/env python

"""
Advent of Code 2017: Day 9 Part 2
https://adventofcode.com/2017/day/9
"""

import sys

with open(sys.argv[1], 'r') as file:
	input = list(file.readline())
	
junk, count = False, 0

# Process input character-by-character
while input:
	token = input.pop(0)
	
	# Check if next token should be ignored
	if token == '!':
		input.pop(0)
		
	# Check if we've opened or closed junk
	elif token == '<' and not junk:
		junk = True
	elif token == '>' and junk:
		junk = False
		
	# Count characters within junk
	elif junk:
		count += 1
		
# Print the final count
print count
