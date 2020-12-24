from matplotlib import pyplot as plt
from pprint import pprint as p
import networkx as nx
import random

sites = {}
#  open_sites = []
open_sites = {}
#  closed_sites = []
closed_sites = {}
bonds = []

size = 40
spacing = 1
p = 0.75

size_x = size 
size_y = size

for x_i in range(size_x):
    for y_i in range(size_y):
        sites[(x_i, y_i)] = (x_i*spacing, y_i*spacing)

        site_open = True if random.random() < p else False

        if site_open:
            #  open_sites.append((x_i, y_i))
            open_sites[(x_i, y_i)] = (x_i*spacing, y_i*spacing)
        else:
            #  closed_sites.append((x_i, y_i))
            closed_sites[(x_i, y_i)] = (x_i*spacing, y_i*spacing)

        if x_i < size_x - 1 and y_i < size_y - 1:
            bonds.append(((x_i, y_i), (x_i + 1, y_i)))
            bonds.append(((x_i, y_i), (x_i, y_i + 1)))
        if x_i == size_x - 1 and y_i < size_y - 1:
            bonds.append(((x_i, y_i), (x_i, y_i + 1)))
        if x_i < size_x - 1 and y_i == size_y - 1:
            bonds.append(((x_i, y_i), (x_i + 1, y_i)))


N = nx.Graph()
N.add_nodes_from(sites.keys())
N.add_edges_from(bonds)

#  nx.draw_networkx_nodes(N, sites, nodelist=open_sites.keys(), node_color="black")
#  nx.draw_networkx_nodes(N, sites, nodelist=closed_sites.keys(), node_color="grey")
#  nx.draw_networkx_edges(N, sites)
#  plt.box(on=None)
#  plt.savefig("test.png", bbox_inches="tight")

#  plt.clf()

options = {"node_size": 0.5, "node_color": "black"}

fig, ax = plt.subplots()

N.remove_nodes_from(closed_sites.keys())
nx.draw_networkx_nodes(N, open_sites, **options)
nx.draw_networkx_edges(N, open_sites, width=0.5)
plt.box(on=None)
ax.set_aspect("equal")
plt.savefig("test.png", bbox_inches="tight", dpi=300)
