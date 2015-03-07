# -*- coding: utf-8 -*-
import sys
import json
import collections

with open(sys.argv[1]) as f:
    line = f.readline()
    frequencies = collections.defaultdict(int)
    total = 0
    while line:
        data =  json.loads(line)
        line = f.readline()
        total += 1
        if not "tsukurepos" in data:
            frequencies[0] += 1
        else:
            frequencies[len(data["tsukurepos"])] += 1
    # frequencies["total"] = total
    for val in sorted(frequencies.items()):
        print "%s,%s" % val
