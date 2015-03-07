# -*- coding: utf-8 -*-
import sys
import json
import collections

with open(sys.argv[1]) as f:
    line = f.readline()
    frequencies = collections.defaultdict(int)
    while line:
        data =  json.loads(line)
        line = f.readline()
        frequencies[data["published_at"][:4]] += 1
    for val in sorted(frequencies.items()):
        print "%s,%s" % val
