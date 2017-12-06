#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as file:
	input_list = file.readlines()
	
	
# Part 1: Find passphrases without repeats

count = 0

for input in input_list:
	
	phrase_list = input.split()
	phrase_dict = {}
	
	valid = 1
	for phrase in phrase_list:
		
		if phrase not in phrase_dict:
			phrase_dict[phrase] = None
		else:
			valid = 0
			break
			
	count += valid
	
print '%d/%d' % (count, len(input_list))


# Part 2: Find passphrases without repeats or anagrams

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
	
print '%d/%d' % (count, len(input_list))
