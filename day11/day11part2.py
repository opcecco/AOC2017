#!/usr/bin/env python

"""
Advent of Code 2017: Day 11 Part 2
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
	
movement_dict = {}
max_distance = 0

for step in input:
	
	# Add the next step to the movement dictionary
	movement_dict[step] = movement_dict.get(step, 0) + 1
	
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
				
	# Remove non-moves from dictionary and check if the current distance is the max
	movement_dict[None] = 0
	this_distance = sum(movement_dict.values())
	if this_distance > max_distance:
		max_distance = this_distance
		
# Print the maximum distance
print max_distance
