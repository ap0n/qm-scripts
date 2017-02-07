#!/usr/bin/python

import sys

if len(sys.argv) != 2:
	print "Usage: python check_symbol_list.py <path_of_dataset>"
	exit()

path = sys.argv[1]
symbols_file = open(path + "/Symbollist.txt")
data_file = open(path + "/data.txt")

symbols_nl = symbols_file.readlines()
symbols = []
for s in symbols_nl:
	symbols.append(s.strip())

errors = False
data = data_file.readlines()
for line in data:
	s = line.split(",")[0]
	if s not in symbols:
		print s + ' not in symbols list!'
		errors = True

if errors:
	print "Erros where found!"
else:
	print "All ok"

symbols_file.close()
data_file.close()
