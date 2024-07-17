# Asignacion de Programacion 1 (PA1) - Alcibiades Bustillo - COMP6785
# Creado por: Christian Robles

from LinkedList import LinkedList

# Variables Globales
time = 0 # contador de los pasos del algoritmo
t_order = LinkedList() # lista para el orden topologico

# DFS(G)
# Aplica 'Breath First Search' a un grafo G dado. El proposito
# en este caso es determinar el order topologico del grafo si 
# alguno, y a su ves identificar si el grafo tiene ciclos.
# Entrada:
# 	G - instancia de la clase Graph
# Salida:
# 	devuelve un booleano que indica si se encontraron o no ciclos
#	en el grafo, y una lista enlazada con el orden topologico de
# 	haber alguno.
def DFS(G):
	for v in G.V():
		v.color = 'white'
		v.pred = None
	for v in G.V():
		if v.color == 'white':
			if _DFS_visit(G, v):
				return True, t_order
	return False, t_order

# _DFS_vist(G, v)
# Funcion recursiva que ayuda al DFS(G).
# Entrada:
# 	G - instancia de la clase Graph
#	v - vertice de G, instancia de Vertex
# Salida:
# 	devuelve un booleano que indica si se encontraron o no ciclos
#	en el grafo
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
