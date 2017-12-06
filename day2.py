#!/usr/bin/env python

import sys

with open(sys.argv[1]) as file:
	spreadsheet = [[int(num) for num in row.split()] for row in file.readlines()]
	
	
# Part 1: Find greatest difference

checksum = sum([max(row) - min(row) for row in spreadsheet])
print checksum


# Part 2: Find two numbers that evenly divide

checksum = 0

for row in spreadsheet:
	for i in xrange(len(row)):
		
		num = row[i]
		divisors = row[:i] + row[i + 1:]
		
		for d in divisors:
			if num % d == 0:
				checksum += num / d
				
print checksum
