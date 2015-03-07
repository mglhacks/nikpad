# -*- coding: utf-8 -*-
import json
import sys

from collections import defaultdict

def get_ingredients(recipe):
    """Return list of ingredients"""
    ings = []
    if "ingredients" in recipe:
        for ingredient in recipe["ingredients"]:
            ings.append(ingredient["name"])
    return ings

def calculate_frequencies(in_file):
    frequencies = defaultdict(int)
    line = in_file.readline()
    total = 0
    while line:
        total += 1
        recipe = json.loads(line)
        ingredients = get_ingredients(recipe)
        for ingredient in ingredients:
            frequencies[ingredient] += 1
        line = in_file.readline()
    return (sorted(frequencies.items(), key=lambda x:x[1], reverse=True), total)

def print_pairs(pairs, out_file, total, limit=0):
    count = 0
    if limit == 0:
        limit = len(pairs)
    print >> out_file, "# ing, proportion, count, total"
    for pair in pairs:
        count += 1
        if count > limit:
            break
        print >> out_file, "%s,%.6f,%s,%s"%(repr(pair[0].encode(sys.stdout.encoding) if isinstance\
                                                 (pair[0], basestring) else pair[0]).decode('string-escape'),\
                                            pair[1] / float(total),
                                            pair[1],
                                            total)

in_file = open(sys.argv[1], "r")
out_file = open("data_use/ingredients_count.csv", "w")

frequencies, total = calculate_frequencies(in_file)
print_pairs(frequencies, out_file, total)

in_file.close()
out_file.close()
