#!/usr/bin/env python

"""
Advent of Code 2017: Day 8 Part 2
https://adventofcode.com/2017/day/8
"""

import sys

# Run an instruction (including its condition)
def run_instruction(register, operation, value, cond_register, cond_comparison, cond_value):
	global register_dict
	global highest
	
	compare_func = {
		'>': lambda a, b: a > b,
		'<': lambda a, b: a < b,
		'>=': lambda a, b: a >= b,
		'<=': lambda a, b: a <= b,
		'==': lambda a, b: a == b,
		'!=': lambda a, b: a != b,
	}[cond_comparison]
	
	if compare_func(register_dict.get(cond_register), cond_value):
		if operation == 'inc':
			register_dict[register] += value
		else:
			register_dict[register] -= value
			
	if register_dict[register] > highest:
		highest = register_dict[register]
		
		
with open(sys.argv[1], 'r') as file:
	input = [line.split() for line in file.readlines()]
	
# Initialize all registers to zero
register_name_set = set([instruction[0] for instruction in input])
register_dict = dict(zip(register_name_set, [0] * len(register_name_set)))
highest = 0

# Run all instructions
for instruction in input:
	run_instruction(instruction[0], instruction[1], int(instruction[2]), instruction[4], instruction[5], int(instruction[6]))
	
print highest
