#!/usr/bin/env python

"""
Advent of Code 2017: Day 3 Part 2
https://adventofcode.com/2017/day/3
"""

import sys, math

input = int(sys.argv[1])

# Initialize grid
ring = int(math.floor(math.ceil(math.sqrt(input))/2))
grid = [[0] * (2 * ring + 1) for i in xrange(2 * ring + 1)]

row_index = ring
col_index = ring
grid[row_index][col_index] = 1

# Define directions
down, right, up, left = (1, 0), (0, 1), (-1, 0), (0, -1)
direction_table = [down, right, up, left]
direction = 0

# Generate spiral using moving cursor
while grid[row_index][col_index] <= input:
	
	new_direction = (direction + 1) % 4
	if grid[row_index + direction_table[new_direction][0]][col_index + direction_table[new_direction][1]] == 0:
		direction = new_direction
		
	row_index, col_index = row_index + direction_table[direction][0], col_index + direction_table[direction][1]
	grid[row_index][col_index] = sum(sum(row[col_index - 1:col_index + 2]) for row in grid[row_index - 1:row_index + 2])
	
print grid[row_index][col_index]
