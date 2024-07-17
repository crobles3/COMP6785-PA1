# Asignacion de Programacion 1 (PA1) - Alcibiades Bustillo - COMP6785
# Creado por: Christian Robles

# _BFS(G, s)
# Aplica 'Breath First Search' a un grafo G dado,
# comenzando en el vertice s. En este caso se utiliza
# para visitar todos los vertices que se pueden alcanzar
# desde s, resultando en la identificacion de un componente 
# conexo de G.
# Entrada:
# 	G - instancia de la clase Graph
# 	s - vertice de G, instancia de Vertex
# Salida:
# 	No devuelve nada, pero modifica algunos vertices de 
# 	G, aquellos que se pueden visitar desde s
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
# Calcula en numero de componentes conexos que
# se encuentran en el grafo dado G.
# Entrada:
# 	G - instancia de la clase Graph
# Salida:
# 	cantidad de componentes conexos 
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
