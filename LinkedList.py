# Asignacion de Programacion 1 (PA1) - Alcibiades Bustillo - COMP6785
# Creado por: Christian Robles

# _Node
# Clase utilizada para representar los nodos de 
# una lista enlazada.
# Variables:
# 	self.__value - valor asignado al nodo
# 	self.__next  - referencia al proximo nodo
class _Node:
	# __init__(self, value, node) [constructor de la clase]
	# Crea una instancia de un nodo, asignandole un valor y
	# una referencia al nodo que le sigue. 
	# Entrada:
	# 	value - valor a ser asignado
	# 	node  - instancia siguiente de _Node
	def __init__(self, value, node=None):
		self.__value = value
		self.__next = node

	# get_value(self)
	# Devuelve el valor de la nodo
	# Salida:
	# 	valor del node
	def get_value(self):
		return self.__value

	# get_next(self)
	# Devuelve el nodo siguiente
	# Salida:
	# 	referencia al nodo siguiente
	def get_next(self):
		return self.__next

	# set_value(self, value)
	# Asigna un nuevo valor al nodo
	# Entrada:
	# 	value - nuevo valor del node
	def set_value(self, value):
		self.__value = value

	# set_next(self, node)
	# Asigna un nuevo nodo siguiente
	# Entrada:
	# 	node - referencia al nuevo nodo siguiente
	def set_next(self, node):
		self.__next = node



# LinkedList
# Clase que implementa la estructura de datos lista enlazada
# Variables:
# 	self.__size - tamaño de la lista
# 	self.__head - referencia al primer nodo de la lista
#	self.__n 	- referencia a un nodo para el iterador
class LinkedList:
	# __init__(self) [constructor de la clase]
	# Crea una instancia de una lista enlazada y la inicializa
	def __init__(self):
		self.__size = 0
		self.__head = None

	# __iter__(self)
	# Asigna el valor inicial del iterador
	def __iter__(self):
		self.__n = self.__head
		return self

	# __next__(self)
	# Se encarga de actualizar el valor del iterador y
	# maneja el caso cuando se termina de iterar la list.
	def __next__(self):
		if self.__n != None:
			node = self.__n
			self.__n = node.get_next()
			return node.get_value()
		else:
			raise StopIteration

	# __repr__(self)
	# Maneja como se va a representar la lista cuando
	# se imprime en la consola, por ejemplo.
	def __repr__(self):
		arr = self.to_array()
		arr.append('None')
		return ' -> '.join(arr)

	# add_element(self, elem):
	# Añade un nuevo elemento al final de la lista.
	# Entrada:
	# 	elem - elemento a ser añadido
	# Salida:
	# 	booleano indicando si el elemento se añadio
	#	exitosamento o no.
	def add_element(self, elem):
		new_node = _Node(elem)
		if self.__head == None:
			self.__head = new_node
		else:
			node = self.__head
			while node.get_next() != None:
				node = node.get_next()
			node.set_next(new_node)
		self.__size += 1
		return True

	# add_at(self, pos, elem):
	# Añade un nuevo elemento en una posicion dada de la lista.
	# Entrada:
	# 	pos  - posicion de la lista donde se desea añadir
	# 	elem - elemento a ser añadido
	# Salida:
	# 	booleano indicando si el elemento se añadio
	#	exitosamento o no.
	def add_at(self, pos, elem):
		if pos < 0 or pos > self.__size:
			return False
		new_node = _Node(elem)
		if pos == 0 or self.__size == 0:
			new_node.set_next(self.__head)
			self.__head = new_node
			self.__size += 1
			return True
		node = self.__head
		for _ in range(pos-1):
			node = node.get_next()
		new_node.set_next(node.get_next())
		node.set_next(new_node)
		self.__size += 1
		return True

	# remove_element(self, elem):
	# Elimina un elemento de la lista dado el elemento.
	# Entrada:
	# 	elem - elemento a ser eliminado
	# Salida:
	# 	booleano indicando si el elemento se elimino
	#	exitosamento o no.
	def remove_element(self, elem):
		node = self.__head
		if node.get_value() == elem:
			self.__head = node.get_next()
			self.__size -= 1
			return True
		while node.get_next() != None:
			next_node = node.get_next()
			if next_node.get_value() == elem:
				node.set_next(next_node.get_next())
				self.__size -= 1
				return True
			node = next_node
		return False

	# remove_from(self, pos):
	# Elimina un elemento de la lista dado una posicion.
	# Entrada:
	# 	pos - posicion de la lista de donde se desea remover
	# Salida:
	# 	booleano indicando si el elemento se elimino
	#	exitosamento o no.
	def remove_from(self, pos):
		if pos < 0 or pos >= self.__size:
			return False
		node = self.__head
		if pos == 0:
			self.__head = node.get_next()
			self.__size -= 1
			return True
		for _ in range(pos-1):
			node = node.get_next()
		next_node = node.get_next()
		node.set_next(next_node.get_next())
		self.__size -= 1
		return True

	# index_of(self, elem)
	# Devuelve la posicion de un elemento dado en la lista.
	# Entrada:
	# 	elem - elemento que se desea encontrar
	# Salida:
	# 	posicion en la lista del elemento dado, o -1 si el 
	#	elemento no se encuentra en la lista
	def index_of(self, elem):
		node, i = self.__head, 0
		while node != None:
			if(node.get_value() == elem):
				return i
			node = node.get_next()
			i += 1
		return -1

	# elem_at(self, pos)
	# Devuelve el elemento que se encuentra en una posicion dada de la lista.
	# Entrada:
	# 	pos - posicion en la lista en la cual se desea buscar
	# Salida:
	# 	elemento de la lista en la posicion dada, o None si la 
	#	posicion se sale de los limites de la lista
	def elem_at(self, pos):
		if pos < 0 or pos >= self.__size:
			return None
		node = self.__head
		for _ in range(pos):
			node = node.get_next()
		return node.get_value()

	# contains(self, elem)
	# Verifica si el elemento dado esta en la lista.
	# Entrada:
	# 	elem - elemento que se desea encontrar
	# Salida:
	# 	Booleano indicando si el elemento se encontro o no
	def contains(self, elem):
		return self.index_of(elem) > -1

	# size(self)
	# Devuelve el tamaño de la lista.
	# Salida:
	# 	tamaño de la lista
	def size(self):
		return self.__size

	# empty(self)
	# Elimina todos los elementos de la lista.
	def empty(self):
		while self.__head != None:
			self.remove_from(0)

	# to_array(self)
	# Devuelve un arreglo con los elementos de la lista
	# Salida:
	# 	arreglo con los elementos de la lista
	def to_array(self):
		array = []
		for elem in self:
			array.append(str(elem))
		return array



