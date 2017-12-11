#!/usr/bin/env python

"""
Advent of Code 2017: Day 3 Part 1
https://adventofcode.com/2017/day/3
"""

import sys, math

input = int(sys.argv[1])

ring = 0
max_ring_val = 1

# Find while ring/layer our number is in
ring = int(math.floor(math.ceil(math.sqrt(input)) // 2))

# Do some arithmetic to find distance from center
sequence_index = (input - 1) % (2 * ring)
dist_along_edge = abs(sequence_index - ring)
taxi_dist = dist_along_edge + ring

print taxi_dist
