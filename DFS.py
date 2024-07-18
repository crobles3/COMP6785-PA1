# Programming Assignment 1 (PA1) - Alcibiades Bustillo - COMP6785
# Created by: Christian Robles

from LinkedList import LinkedList

# Global variables
time = 0 # algorithm step counter
t_order = LinkedList() # topological order list

# DFS(G)
# Applies 'Breath First Search' to a given graph G. The purpose
# is to determine the topological order of the graph, if any,
# while also verifying if there is any cycle in the graph.
# Parameters:
# 	G - graph, instance of Graph.
# Return:
# 	Returns a boolean that indicates if there was a cycle found
#	in the graph,and a linked list with the topological order,
# 	if any.
def DFS(G):
	for v in G.V():
		v.color = 'white'
		v.pred = None
	for v in G.V():
		if v.color == 'white':
			if _DFS_visit(G, v):
				return True, t_order
	return False, t_order

# _DFS_visit(G, v)
# DFS helper function.
# Parameters:
# 	G - graph, instance of Graph.
#	v - node of G, instance de Vertex
# Returns:
# 	Returns a boolean that indicate of a cycle was found.
def _DFS_visit(G, v):
	global time, t_order
	v.color = 'gray'
	time += 1
	v.d = time
	for u in G.Adj(v):
		if u.color == 'white':
			u.pred = v
			if _DFS_visit(G, u):
				return True
		elif u.color == 'gray':
			if(G.is_directed() or v.pred != u):
				return True
	v.color = 'black'
	time += 1
	v.f = time
	t_order.add_at(0, v)
	return False
