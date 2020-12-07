import time

t0 = time.time()

import numpy as np
import pandas as pd
import pandana

nodes = pd.read_csv('nodes.csv', index_col='id_int')
edges = pd.read_csv('edges.csv')

net = pandana.Network(nodes.x, nodes.y, edges.from_int, edges.to_int, edges[['weight']])

n = 1000000

nodes_a = np.random.choice(nodes.index, n)
nodes_b = np.random.choice(nodes.index, n)

tt = net.shortest_path_lengths(nodes_a, nodes_b)

print(round(time.time()-t0))
