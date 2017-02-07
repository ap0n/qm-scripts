#!/usr/bin/python
import sys

if len(sys.argv) != 2:
	print "Usage: python generate_symbol_list.py <path_of_dataset>"
	exit()

path = sys.argv[1]

symbols_file = open(path + "/Symbollist.txt", 'w')
data_file = open(path + "/data.txt")

symbols = set()

data = data_file.readlines()
for line in data:
	symbols.add(line.split(",")[0])
data_file.close()

for l in symbols:
	symbols_file.write(l+'\n')

symbols_file.close()

