# -*- coding: utf-8 -*-

"""recipes.py: Recipe data analysis scripts"""

import requests # Requests is recommended over urllib*
import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

def recipepuppy_api(query='', ingredients=[], page=1):
    """Recipe Puppy API:
    documentation: http://www.recipepuppy.com/about/api/"""
    base_url = 'http://www.recipepuppy.com/api/'
    params = {'p' : page}
    if len(ingredients) > 0:
        params['i'] = ','.join(ingredients)
    if len(query) > 0:
        params['q'] = query
    response = requests.get(base_url, params=params)
    return response.json()

def collector():
    """API data collector method """
    for page in range(1, 101):
        with open('data/page%s.txt'%(page), 'w') as outfile:
            recipes = recipepuppy_api(page=page)
            json.dump(recipes, outfile, indent=2)

def output_graph():
    G=nx.Graph()
    G.add_edges_from([(1,2),(1,3),(1,4),(3,4)])
    G.nodes(data=True)
    G.node[1]['attribute']='value'
    G.nodes(data=True)
    # nx.write_graphml(G,'so.graphml')
    labels={}
    labels[0]=r'$a$'
    labels[1]=r'$b$'
    labels[2]=r'$c$'
    labels[3]=r'$d$'
    nx.draw_networkx(G)
    plt.axis('off')
    plt.savefig("path.pdf")

def load_recipes():
    recipes = []
    for page in range(1, 2):
        with open('data/page%s.txt'%(page), 'r') as infile:
            res = json.load(infile)
            [recipes.append(r['ingredients']) for r in res['results']]
    return recipes

def analyze_recipes(recipes):
    ingredients = []
    for r in recipes:
        ingredients.extend(r.split(', '))

def build_graph(recipes):
    all_i = []
    G = nx.Graph()
    for r in recipes:
        ingredients = r.split(', ')
        all_i.extend(ingredients)
        l = len(ingredients)
        for i in range(l):
            for j in range(i + 1, l):
                if not G.has_edge(ingredients[i], ingredients[j]):
                    G.add_edge(ingredients[i], ingredients[j], weight=1)
                else:
                    G[ingredients[i]][ingredients[j]]['weight'] += 1
    count = Counter(all_i).most_common()
    G.occurences = {}
    for key, value in count:
        G.occurences[key] = value
    return G

def draw_graph(G):
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, node_size=[G.occurences[v]*100 for v in G], font_size=10)
    # nx.draw_networkx_edge_labels(G, pos)
    plt.axis('off')
    plt.savefig("recipes.pdf")

recipes = load_recipes()
G = build_graph(recipes)
draw_graph(G)
