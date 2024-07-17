# Asignacion de Programacion 1 (PA1) - Alcibiades Bustillo - COMP6785
# Creado por: Christian Robles

from LinkedList import LinkedList

# Vertex
# Clase utilizada para representar los vertices de 
# un grafo.
# Variables:
# 	self.__val - valor asignado al vertice
class Vertex:
	# __init__(self, value) [constructor de la clase]
	# Crea una instancia de un vertice, asignandole un valor
	# Entrada:
	# 	value - valor a ser asignado
	def __init__(self, value):
		self.__val = value

	# __repr__(self)
	# Maneja como se va a representar vertice cuando
	# se imprime en la consola, por ejemplo.
	def __repr__(self):
		return str(self.__val)

	# get_value(self)
	# Devuelve el valor del vertice
	# Salida:
	# 	valor del vertice
	def get_value(self):
		return self.__val


# Graph
# Clase que implementa la estructura de datos grafo
# Variables:
# 	self.__V 		- lista de los vertices del grafo
# 	self.__E 		- lista de las aristas del grafo
# 	self.__Adj		- listas de adyacencia en forma de diccionario
# 	self.__directed - indicador booleano de si el grafo es o no es dirigido
class Graph:
	# __init__(self) [constructor de la clase]
	# Crea una instancia de un grafo y lo inicializa
	# Entrada:
	# 	is_dir - indicador booleano de si es o no dirigido el grafo
	def __init__(self, is_dir = False):
		self.__V = []
		self.__E = []
		self.__Adj = {}
		self.__directed = is_dir

	# __repr__(self)
	# Maneja como se va a representar el grafo cuando
	# se imprime en la consola, por ejemplo.
	def __repr__(self):
		vertices = ', '.join(map(lambda v: str(v.get_value()), self.__V))
		edges = '\n'.join(map(lambda e: '({} {})'.format(e[0], e[1]), self.__E))
		return '\nVertices:\n' + vertices + '\n\nEdges:\n' + edges

	# add_vertex(self, value):
	# Añade un nuevo vertice al grafo y crea la lista de adyacencia
	# respectiva a dicho vertice, si el vertice no existe.
	# Entrada:
	# 	value - valor del nuevo vertice
	def add_vertex(self, value):
		_, v = self.find_vertex(value)
		if v == None:
			v = Vertex(value)
			self.__V.append(v)
			self.__Adj[value] = LinkedList()

	# find_vertex(self, value):
	# Encuentra el vertice que concide con el valor dado.
	# Entrada:
	# 	value - valor del vertice que se decea buscar
	# Salida:
	#	posicion del vertice y el vertice que concide con
	#	el valor dado, de no concidir devuelve -1 y None
	def find_vertex(self, value):
		i = 0
		for v in self.__V:
			if v.get_value() == value:
				return i, v
			i += 1
		return -1, None

	# remove_vertex(self, value):
	# Remueve el vertice que concide con el valor dado, y de igual
	# manera lo remueve de las listas de adyacencia correspondientes.
	# Entrada:
	# 	value - valor del vertice que se decea eliminar
	# Salida:
	#	booleano indicando si el vertice se logro eliminar o no.
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
	# Añade una arista con los valores dados para los cuales 
	# existen vertices en el grafo, y añade los vertices a las 
	# listas de adyacencia correspondientes.
	# Entrada:
	# 	tail  - valor del vertice del cual sale la arista
	# 	point - valor del vertice en el cual incide la arista
	# Salida:
	#	booleano indicando si la arista se logro añadir o no.
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
	# Remueve la arista con los valores dados para los cuales 
	# existen vertices en el grafo, y elimina los vertices de las 
	# listas de adyacencia correspondientes.
	# Entrada:
	# 	tail  - valor del vertice del cual sale la arista
	# 	point - valor del vertice en el cual incide la arista
	# Salida:
	#	booleano indicando si la arista se logro eliminar o no.
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
	# Devuelve la lista de vertices del grafo
	# Salida:
	# 	lista de vertices del grafo
	def V(self):
		return self.__V

	# E(self)
	# Devuelve la lista de aristas del grafo
	# Salida:
	# 	lista de aristas del grafo
	def E(self):
		return self.__E

	# is_directed(self)
	# Devuelve si el grafo es o no dirirgido
	# Salida:
	#	booleano indicando si el grafo es o no dirigido
	def is_directed(self):
		return self.__directed

	# Adj(self, v)
	# Devuelve la lista de adyacencia correspondiente a un
	# vertice dado.
	# Entrada:
	# 	v - vertice o valor del vertice de interes
	# Salida:
	#	lista de adyacencia correspondiente al vertice dado
	def Adj(self, v):
		if isinstance(v, Vertex):
			return self.__Adj[v.get_value()]
		else:
			return self.__Adj[v]



