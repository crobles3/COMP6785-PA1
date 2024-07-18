# Programming Assignment 1 (PA1) - Alcibiades Bustillo - COMP6785
# Created by: Christian Robles

# _BFS(G, s)
# Applies 'Breath First Search' a given graph G,
# starting with node s. In this case it is used to
# visit all the nodes that can be reached from s,
# in order to identify a connected component of G.
# Parameters:
# 	G - graph, instance of Graph.
# 	s - node of G, instance of Vertex.
# Returns:
# 	No return, but it modifies the nodes
# 	that can be visited from s.
def _BFS(G, s):
	s.color = 'gray'
	s.d = 0
	s.pred = None 
	Q = [s]
	while len(Q):
		u = Q.pop(0)
		for v in G.Adj(u):
			if v.color == 'white':
				v.color = 'gray'
				v.d = u.d + 1
				v.pred = u
				Q.append(v)
		u.color = 'black'

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
			_BFS(G, v)
	return c
