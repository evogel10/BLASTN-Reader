#!/usr/bin/env python3

import re

# Opens the file to read only
blastn_file = open('example_blast.txt', 'r')

# Instantiates the query ID, acceccion number, sequence length, 
# and score varibles
queryID = ''
accNums = []
lengths = []
scores = []

# Reads through the file line by line
for line in blastn_file:

	# Removes whitespace from both ends
	line = line.strip()

	# Searches for the query ID
	m = re.search(r'Query= (\w+)', line)
	if m:
		# Adds the query ID from the regex search
		queryID = m.group(1)

	# Searches for the accession numbers of the alignments
	m = re.match(r'>(.*\|)', line)
	if m:
		# Adds the accession number to the accNum list from the regex 
		# search
		accNums.append(m.group(1))

	# Searches for the lengths of the query and alignments
	m = re.search(r'Length=(\d+)', line)
	if m:
		# Adds the lengths to the lengths list from the regex search
		lengths.append(m.group(1))

	# Searches for the scores of the alignments
	m = re.search(r'Score = (\s*) (\d+)', line)
	if m:
		# Adds the scores to the scores list from the regex search
		scores.append(m.group(2))

# Prints the query ID and length
print('\nQuery ID: %s' % queryID)
print('Query Length: %s\n' % lengths[0])

# Loops through the first 10 alignments and prints the alignment 
# number, accession number, length, and score
for x in range(1,11):
	print('Alignment #%d: Accession = %s (Length = %s, Score = %s)'
	 % (x, accNums[x-1], lengths[x], scores[x-1]))
print('')

# Closes the file
blastn_file.close()