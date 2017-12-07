#!/usr/bin/env python

"""
Advent of Code 2017: Day 7 Part 1
https://adventofcode.com/2017/day/7
"""

import sys, re

# Define Node class to store tower information
class Node:
	
	def __init__(self, name, weight, holding):
		self.name = name
		self.weight = weight
		self.holding = holding
		self.parent = None
		
	def find_root(self):
		return self if self.parent is None else self.parent.find_root()
		
		
tree_dict = {}

# Parse input file into Nodes
with open(sys.argv[1], 'r') as file:
	for line in file.readlines():
		line_vals = re.findall(r'\w+', line)
		tree_dict[line_vals[0]] = Node(line_vals[0], int(line_vals[1]), line_vals[2:])
		
# Find all Node parents
for name in tree_dict:
	for holding_name in tree_dict[name].holding:
		tree_dict[holding_name].parent = tree_dict[name]
		
# Find root node
print tree_dict[name].find_root().name
