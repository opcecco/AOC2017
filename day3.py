#!/usr/bin/env python

import sys

input = int(sys.argv[1])


# Part 1: Find distance from center of spiral

ring = 0
max_ring_val = 1

while max_ring_val < input:
	ring += 1
	max_ring_val += 8 * ring
	
sequence_index = (input - 1) % (2 * ring)
dist_along_edge = abs(sequence_index - ring)
taxi_dist = dist_along_edge + ring

print taxi_dist


# Part 2: Find local sums

grid = [[0] * (2 * (taxi_dist + 1)) for i in xrange(2 * (taxi_dist + 1))]
grid[0][0] = 1
grid[0][1] = 1

row_index = 0
col_index = 1

up = (-1, 0); down = (1, 0); left = (0, -1); right = (0, 1)
direction = right

while grid[row_index][col_index] <= input:
	
	if direction == right and grid[row_index + up[0]][col_index + up[1]] == 0:
		direction = up
	elif direction == up and grid[row_index + left[0]][col_index + left[1]] == 0:
		direction = left
	elif direction == left and grid[row_index + down[0]][col_index + down[1]] == 0:
		direction = down
	elif direction == down and grid[row_index + right[0]][col_index + right[1]] == 0:
		direction = right
		
	row_index += direction[0]
	col_index += direction[1]
	
	grid[row_index][col_index] = sum([sum([row[col_index - 1], row[col_index], row[col_index + 1]]) for row in [grid[row_index - 1], grid[row_index], grid[row_index + 1]]])
	
print grid[row_index][col_index]
