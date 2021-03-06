#!/usr/bin/env python

"""
Advent of Code 2017: Day 6 Part 1
https://adventofcode.com/2017/day/6
"""

import sys

# Function to redistribute memory
def redistribute(state):
	value = max(state)
	index = state.index(value)
	state[index] = 0
	
	for i in xrange(index + 1, index + value + 1):
		state[i % len(state)] += 1
		
	return state
	
	
with open(sys.argv[1], 'r') as file:
	input = [int(num) for num in file.readline().split()]
	
state_dict = {str(input): None}
count = 1

# Use dictionary to keep track of seen states
while str(redistribute(input)) not in state_dict:
	state_dict[str(input)] = None
	count += 1
	
print count
