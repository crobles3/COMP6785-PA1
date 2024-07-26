# Programming Assignment 1 (PA1) - Alcibiades Bustillo - COMP6785
# Created by: Christian Robles

from . import BFS

# ConnectedComponents(G)
# Counts the number of connected components
# found in a given graph G.
# Parameters:
# 	G - graph, instance of Graph
# Returns:
# 	Number of connected components.
def ConnectedComponent(G):
	for v in G.V():
		v.color = 'white'
		v.d = float('inf')
		v.pred = None 
	c = 0
	for v in G.V():
		if v.color == 'white':
			c += 1
			BFS(G, v)
	return c
