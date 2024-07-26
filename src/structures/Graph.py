# Programming Assignment 1 (PA1) - Alcibiades Bustillo - COMP6785
# Created by: Christian Robles

from . import LinkedList

# Vertex
# Class used to represent the nodes of the graph. 
# Variables:
# 	self.__val - node value
class _Vertex:
	# __init__(self, value) [class constructor]
	# Create an instance od Vertex, assigning a value.
	# Parameters:
	# 	value - node value to be assigned.
	def __init__(self, value):
		self.__val = value

	# __repr__(self)
	# Manages how the node is displayed.
	def __repr__(self):
		return str(self.__val)

	# get_value(self)
	# Returns the value of the node.
	# Returns:
	# 	Value of the node.
	def get_value(self):
		return self.__val


# Graph
# Class that implements a Graph DS.
# Variables:
# 	self.__V 		- list of nodes
# 	self.__E 		- list of edges
# 	self.__Adj		- adjacency list
# 	self.__directed - boolean indicating if the graph is directed or not.
class Graph:
	# __init__(self) [class constructor]
	# Creates and initializes an instance of the graph.
	# Parameters:
	# 	is_dir - boolean indicating if os directed or not
	def __init__(self, is_dir = False):
		self.__V = []
		self.__E = []
		self.__Adj = {}
		self.__directed = is_dir

	# __repr__(self)
	# Manages how the graph is displayed.
	def __repr__(self):
		vertices = ', '.join(map(lambda v: str(v.get_value()), self.__V))
		edges = '\n'.join(map(lambda e: '({} {})'.format(e[0], e[1]), self.__E))
		return '\nVertices:\n' + vertices + '\n\nEdges:\n' + edges

	# add_vertex(self, value):
	# Adds a new node to the graph and creates an adjacency
	# list respectively if the node is didn't exist.
	# Parameters:
	# 	value - new node value.
	def add_vertex(self, value):
		_, v = self.find_vertex(value)
		if v == None:
			v = _Vertex(value)
			self.__V.append(v)
			self.__Adj[value] = LinkedList()

	# find_vertex(self, value):
	# Finds the node corresponding to the given value.
	# Parameters:
	# 	value - desired node value.
	# Return:
	#	The node's position, and it's Vertex instance.
	#	If not found it returns -1 y None.
	def find_vertex(self, value):
		i = 0
		for v in self.__V:
			if v.get_value() == value:
				return i, v
			i += 1
		return -1, None

	# remove_vertex(self, value):
	# Removes the Vertex instance and the adjacency list corresponding
	# to the provided value.
	# Parameters:
	# 	value - value of the node that will be removed.
	# Returns:
	#	Boolean indicating if the removal was successful or not.
	def remove_vertex(self, value):
		i, v = self.find_vertex(value)
		if v is None:
			return False
		for u in self.__V:
			if u != v:
				adj = self.__Adj[u.get_value()]
				adj.remove_element(v)
		del self.__V[i]
		del self.__Adj[value]
		return True

	# add_edge(self, tail, point):
	# Adds the edge corresponding to the given node value pair
	# that must be already part of the graph, and adds them to
	# the corresponding adjacency list.
	# Parameters:
	# 	tail  - node value from where the edge comes from
	# 	point - node value from where the edge goes to
	# Returns:
	#	Boolean indicating if the edge was added successfully or not.
	def add_edge(self, tail, point):
		_, v = self.find_vertex(tail)
		if v is None:
			return False
		_, u = self.find_vertex(point)
		if u is None:
			return False
		adj = self.__Adj[tail]
		adj.add_element(u)
		if not self.__directed:
			adj = self.__Adj[point]
			adj.add_element(v)
		self.__E.append((tail, point))
		return True

	# remove_edge(self, tail, point):
	# Removes the edge corresponding from the given node value pair
	# that must be already part of the graph, and removes them from
	# the corresponding adjacency list.
	# Parameters:
	# 	tail  - node value from where the edge comes from
	# 	point - node value from where the edge goes to
	# Returns:
	#	Boolean indicating if the edge was removed successfully or not.
	def remove_edge(self, tail, point):
		_, v = self.find_vertex(tail)
		if v is None:
			return False
		_, u = self.find_vertex(point)
		if u is None:
			return False
		adj = self.__Adj[tail]
		adj.remove_element(u)
		if not self.__directed:
			adj = self.__Adj[point]
			adj.remove_element(v)
		self.__E.remove((tail, point))
		return True

	# V(self)
	# Returns the list of nodes of the graph.
	# Returns:
	# 	Node's list.
	def V(self):
		return self.__V

	# E(self)
	# Returns the list of edges corresponding to the graph.
	# Returns:
	# 	List of edges.
	def E(self):
		return self.__E

	# is_directed(self)
	# Return if the graph is directed or not.
	# Returns:
	#	Boolean indicating if the graph is directed or not.
	def is_directed(self):
		return self.__directed

	# Adj(self, v)
	# Returns adjacency list corresponding to the given node.
	# Parameters:
	# 	v - value of Vertex instance of the node.
	# Returns:
	#	Adjacency list.
	def Adj(self, v):
		if isinstance(v, _Vertex):
			return self.__Adj[v.get_value()]
		else:
			return self.__Adj[v]



