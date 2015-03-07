# -*- coding: utf-8 -*-

def load_all(NAMES, NODE_SIZES, limit=0):
    in_file = open("../data_use/ingredients_count_2013.csv", "r")

    line = in_file.readline()
    count = 0
    while line:
        count += 1
        if count == 1:
            line = in_file.readline()
            continue # ignore first line
        if limit != 0 and count > limit:
            break
        parts = line.split(',')
        NAMES.append(parts[0].decode('utf-8', "replace"))
        NODE_SIZES.append(parts[1])
        line = in_file.readline()
    in_file.close()
