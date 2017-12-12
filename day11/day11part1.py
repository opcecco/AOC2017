#!/usr/bin/env python

"""
Advent of Code 2017: Day 11 Part 1
https://adventofcode.com/2017/day/11
"""

import sys

# Use a dictionary to store how movement steps reduce
reduce_dict = {
	('n', 's',): None,
	('ne', 'sw',): None,
	('se', 'nw',): None,
	('ne', 'nw',): 'n',
	('n', 'se',): 'ne',
	('ne', 's',): 'se',
	('se', 'sw',): 's',
	('nw', 's',): 'sw',
	('n', 'sw',): 'nw',
}

with open(sys.argv[1], 'r') as file:
	input = file.readline().split(',')
	
# Count each movement step and store in dictionary
movement_dict = dict((step, input.count(step),) for step in set(input))

was_reduced = True

# Loop until the movement steps cannot be reduced further
while was_reduced:
	was_reduced = False
	
	# Reduce pairs of movement steps into single steps
	for pair in reduce_dict:
		reduction = min(movement_dict.get(pair[0], 0), movement_dict.get(pair[1], 0))
		
		if reduction > 0:
			movement_dict[pair[0]] -= reduction
			movement_dict[pair[1]] -= reduction
			movement_dict[reduce_dict[pair]] = movement_dict.get(reduce_dict[pair], 0) + reduction
			was_reduced = True
			
# Remove non-moves from dictionary and print total reduced movements
movement_dict[None] = 0
print sum(movement_dict.values())
