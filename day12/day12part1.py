#!/usr/bin/env python

"""
Advent of Code 2017: Day 12 Part 1
https://adventofcode.com/2017/day/12
"""

import sys, re

# Define a Node class to store tree information (parents and children), and to implement union-find
class Node:
	
	def __init__(self):
		self.parent = self
		self.children = []
		
	# Find this node's root
	def find_root(self):
		return self if self.parent is self else self.parent.find_root()
		
	# Merge two nodes' roots into the same tree
	def merge(self, other):
		this_root = self.find_root()
		other_root = other.find_root()
		if this_root is not other_root:
			other_root.parent = this_root
			this_root.children.append(other_root)
			
	# Count all nodes below (and including) this one
	def count_nodes(self):
		return sum(child.count_nodes() for child in self.children) + 1
		
		
with open(sys.argv[1], 'r') as file:
	numeric_regex = re.compile(r'\d+')
	input_list = [[int(num) for num in numeric_regex.findall(line)] for line in file.readlines()]
	
# Create a dictionary of new nodes based on the input
node_dict = dict((input[0], Node()) for input in input_list)

# Merge (union) nodes that are connected
for input in input_list:
	for connected in input[1:]:
		node_dict[input[0]].merge(node_dict[connected])
		
# Print count of nodes in the same group as node 0
print node_dict[0].find_root().count_nodes()
