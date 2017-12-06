#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as file:
	input = [int(line) for line in file.readlines()]
	
	
# Part 1

jumplist = input[:]
index = 0
count = 0

while index >=0 and index < len(jumplist):
	old_index = index
	index += jumplist[index]
	jumplist[old_index] += 1
	count += 1
	
print count


# Part 2

jumplist = input[:]
index = 0
count = 0

while index >=0 and index < len(jumplist):
	old_index = index
	index += jumplist[index]
	
	if jumplist[old_index] >= 3:
		jumplist[old_index] -= 1
	else:
		jumplist[old_index] += 1
		
	count += 1
	
print count
