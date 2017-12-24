#!/usr/bin/env python

"""
Advent of Code 2017: Day 14 Part 2
https://adventofcode.com/2017/day/14
"""

import sys

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
			
			
# Calcualte the knot-hash for a string, using a given formatter
def knot_hash(string):
	data = [ord(character) for character in string] + [17, 31, 73, 47, 23]
	circular_list = range(256)
	current_position, skip_size = 0, 0
	
	# Loop through input lengths, reverse sublists, and move cursor for 64 rounds
	for round in xrange(64):
		for section_length in data:
			
			for i in xrange(current_position, current_position + (section_length // 2)):
				j = 2 * current_position + section_length - i - 1
				circular_list[i % 256], circular_list[j % 256] = circular_list[j % 256], circular_list[i % 256]
				
			current_position += section_length + skip_size
			skip_size += 1
			
	dense_hash = 0
	
	# Calculate the dense hash by XORing blocks of 16 bytes
	for block_start in xrange(0, 256, 16):
		block_value = reduce(lambda a, b: a ^ b, circular_list[block_start:block_start + 16])
		dense_hash <<= 8
		dense_hash += block_value
		
	return dense_hash
	
	
input = sys.argv[1]

node_dict = {}

# Create a hash for each row in the grid
for row in xrange(128):
	hash = '{0:0128b}'.format(knot_hash('%s-%d' % (input, row)))
	
	# Loop through digits in the hash and check for adjacent digits, then merge groups
	for col in xrange(128):
		if hash[col] == '1':
			
			new_node = Node()
			if (row - 1, col) in node_dict:
				node_dict[(row - 1, col)].merge(new_node)
			if (row, col - 1) in node_dict:
				node_dict[(row, col - 1)].merge(new_node)
				
			node_dict[(row, col)] = new_node
			
# Count the total number of groups in the node dictionary
print len([node for node in node_dict.values() if node.parent == node])
