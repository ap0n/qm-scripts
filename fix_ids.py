import errno
import os
import sys

if len(sys.argv) != 2:
    print 'Usage: python fix_ids.py <dataset_directory>'
    sys.exit()

root = sys.argv[1]

data_txt = "/data.txt"
symbollist_txt = "/Symbollist.txt"

names_ids_map = {}
ctr = 0

dir = root + '/fixed/'

try:
    os.makedirs(dir)
except OSError as exc:
    if exc.errno == errno.EEXIST and os.path.isdir(dir):
        pass
    else:
        raise

data_file = open(root + "/" + data_txt)
out_data = open(dir + data_txt, "w+")
with data_file:
    for line in data_file:
        if line == "\n":
            continue
        symbols = line.split(",", 1)
        if len(symbols) != 2:
            print "Error, len(symbols != 2)! symbols: ", symbols
        if symbols[0] not in names_ids_map.keys():
            names_ids_map[symbols[0]] = ctr
            ctr += 1
        id = names_ids_map[symbols[0]]
        out_line = str(id) + "," + symbols[1]
        out_data.write(out_line)
    out_data.close()

out_symbols = open(dir + symbollist_txt, "w+")
with out_symbols:
    for i in range(0, ctr):
        out_symbols.write(str(i) + '\n')
    out_symbols.close()
