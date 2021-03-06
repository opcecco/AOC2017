#!/usr/bin/env python

"""
Advent of Code 2017: Day 4 Part 2
https://adventofcode.com/2017/day/4
"""

import sys

with open(sys.argv[1], 'r') as file:
	input_list = file.readlines()
	
count = 0

for input in input_list:
	
	phrase_list = input.split()
	phrase_dict = {}
	
	valid = 1
	for phrase in phrase_list:
		sorted_phrase = ''.join(sorted(phrase))
		
		if sorted_phrase not in phrase_dict:
			phrase_dict[sorted_phrase] = None
		else:
			valid = 0
			break
			
	count += valid
	
print count
