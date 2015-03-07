# -*- coding: utf-8 -*-
import sys
import json
import collections

def split_into_files(source_file, files):
    line = source_file.readline()
    while line:
        data = json.loads(line)
        files[int(data["published_at"][:4])].write(line)
        line = source_file.readline()

out_files = {}
for year in range(1998, 2015):
    out_files[year] = open("data_extracted/recipe_%s.json"%year, "w")
source_file = open(sys.argv[1], "r")

split_into_files(source_file, out_files)

for out_file in out_files.values():
    out_file.close()
source_file.close()
