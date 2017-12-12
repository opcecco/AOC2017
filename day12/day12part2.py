#!/usr/bin/env python

"""
Advent of Code 2017: Day 12 Part 2
https://adventofcode.com/2017/day/12
"""

import sys, re

# Define a Node class to store tree information (parents and children), and to implement union-find
class Node:
	
	def __init__(self):
		self.parent = self
		
	# Find this node's root
	def find_root(self):
		return self if self.parent is self else self.parent.find_root()
		
	# Merge two nodes' roots into the same tree
	def merge(self, other):
		this_root = self.find_root()
		other_root = other.find_root()
		if this_root is not other_root:
			other_root.parent = this_root
			
			
with open(sys.argv[1], 'r') as file:
	numeric_regex = re.compile(r'\d+')
	input_list = [[int(num) for num in numeric_regex.findall(line)] for line in file.readlines()]
	
# Create a dictionary of new nodes based on the input
node_dict = dict((input[0], Node()) for input in input_list)

# Merge (union) nodes that are connected
for input in input_list:
	for connected in input[1:]:
		node_dict[input[0]].merge(node_dict[connected])
		
# Print the total number of roots (equal to the number of groups)
print len([node for node in node_dict.values() if node.parent == node])
