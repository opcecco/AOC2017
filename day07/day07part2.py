#!/usr/bin/env python

"""
Advent of Code 2017: Day 7 Part 2
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
		self.children = []
		self.cumulative_weight = None
		
	def find_root(self):
		return self if self.parent is None else self.parent.find_root()
		
	def find_cumulative_weight(self):
		if self.cumulative_weight is None:
			self.cumulative_weight = self.weight if len(self.children) == 0 else self.weight + sum(child.find_cumulative_weight() for child in self.children)
		return self.cumulative_weight
		
		
# Recursively finds unbalanced node and returns the weight it needs to be to balance
def find_unbalanced(node, difference = 0):
	if len(node.children) > 0:
		weight_list = [child.find_cumulative_weight() for child in node.children]
		weight_mode = max(weight_list, key = weight_list.count)
		
		for child in node.children:
			if child.find_cumulative_weight() != weight_mode:
				return find_unbalanced(child, difference = child.find_cumulative_weight() - weight_mode)
				
	return node.weight - difference
	
	
tree_dict = {}

# Parse input file into Nodes
with open(sys.argv[1], 'r') as file:
	for line in file.readlines():
		line_vals = re.findall(r'\w+', line)
		tree_dict[line_vals[0]] = Node(line_vals[0], int(line_vals[1]), line_vals[2:])
		
# Find all Node parents and children
for name in tree_dict:
	for holding_name in tree_dict[name].holding:
		tree_dict[holding_name].parent = tree_dict[name]
		tree_dict[name].children.append(tree_dict[holding_name])
		
# Find root node and get adjusted weight
root = tree_dict[name].find_root()
print find_unbalanced(root)
