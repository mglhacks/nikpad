# -*- coding: utf-8 -*-

import json
import numpy as np
import sys

from collections import defaultdict
from operator import itemgetter

def get_recipes_bins(in_file, bins=3):
    """Not used, return numpy array of recipe arrays, first bin contains recipes with most scores"""
    line = in_file.readline()
    recipes = []
    while line:
        recipe = json.loads(line)
        recipe["score"] = get_score(recipe)
        recipes.append(recipe)
        line = in_file.readline()
    recipes.sort(key=itemgetter('score'), reverse=True)
    return np.array_split(np.array(recipes), bins)

def get_ingredients(recipe):
    """Return list of ingredients"""
    ings = []
    if "ingredients" in recipe:
        for ingredient in recipe["ingredients"]:
            ings.append(ingredient["name"])
    return ings

def get_score(recipe):
    """Score of a recipe: just len of 'tsukurepos'"""
    if not "tsukurepos" in recipe:
        return 0
    else:
        return len(recipe["tsukurepos"])

def print_score_pairs(pairs, out_file, limit=0):
    count = 0
    if limit == 0:
        limit = len(pairs)
    print >> out_file, "# [ing1, ing2], count, score"
    for pair in pairs:
        count += 1
        if count > limit:
            break
        print >> out_file,\
            "%s,%s,%s"%(repr([x.encode(sys.stdout.encoding) if isinstance(x, basestring) else x for
                              x in pair[0]]).decode('string-escape'), pair[1]['count'],\
                        pair[1]['score'])

def calculate_pair_scores(in_file):
    """Calculate score for each pairs"""
    scores = defaultdict(lambda : defaultdict(int))
    line = in_file.readline()
    while line:
        recipe = json.loads(line)
        score = get_score(recipe)
        ingredients = get_ingredients(recipe)
        for idx in range(len(ingredients) - 1):
            scores[frozenset([ingredients[idx], ingredients[idx + 1]])]['score'] += score
            scores[frozenset([ingredients[idx], ingredients[idx + 1]])]['count'] += 1
        line = in_file.readline()
    return sorted(scores.items(), key=lambda x:x[1], reverse=True)

in_file = open(sys.argv[1], "r")
out_file = open("data_use/pair_scores.csv", "w")

pair_scores = calculate_pair_scores(in_file)
print_score_pairs(pair_scores, out_file)

# recipe_bins = get_recipes_bins(in_file)

in_file.close()
out_file.close()
