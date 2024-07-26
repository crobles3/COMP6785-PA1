# Programming Assignment 1 (PA1) - Alcibiades Bustillo - COMP6785
# Created by: Christian Robles

# _Node
# Class used to represent nodes in 
# a linked list.
# Variables:
# 	self.__value - value assigned to the node.
# 	self.__next  - reference to the next node.
class _Node:
	# __init__(self, value, node) [class constructor]
	# Creates an instance of a node, assigning it a value
	# and a reference to the next node (if provided). 
	# Parameters:
	# 	value - node's value.
	# 	node  - next node, instance of _Node.
	def __init__(self, value, node=None):
		self.__value = value
		self.__next = node

	# get_value(self)
	# Returns the node's value.
	# Returns:
	# 	Value of the node.
	def get_value(self):
		return self.__value

	# get_next(self)
	# Returns the next node.
	# Returns:
	# 	An instance of _Node corresponding to the next node.
	def get_next(self):
		return self.__next

	# set_value(self, value)
	# Assigns a new value to the node.
	# Parameters:
	# 	value - new value of the node
	def set_value(self, value):
		self.__value = value

	# set_next(self, node)
	# Assigns a new next node to self.
	# Parameters:
	# 	node - reference to the node to be next.
	def set_next(self, node):
		self.__next = node



# LinkedList
# Class that implements the Linked List DS.
# Variables:
# 	self.__size - size of the linked list.
# 	self.__head - reference to the first node of the list.
#	self.__n 	- node reference used in the iterator.
class LinkedList:
	# __init__(self) [class constructor]
	# Create and initializes an instance of LinkedList.
	def __init__(self):
		self.__size = 0
		self.__head = None

	# __iter__(self)
	# Assigns the initial value of the iterator.
	def __iter__(self):
		self.__n = self.__head
		return self

	# __next__(self)
	# Modifies the value of the iterator and manages
	# the case where the iterator has reached the end.
	def __next__(self):
		if self.__n != None:
			node = self.__n
			self.__n = node.get_next()
			return node.get_value()
		else:
			raise StopIteration

	# __repr__(self)
	# Manages how a linked list will be displayed.
	def __repr__(self):
		arr = self.to_array()
		arr.append('None')
		return ' -> '.join(arr)

	# add_element(self, elem):
	# Adds a new element to the end of the list.
	# Parameters:
	# 	elem - new element.
	# Returns:
	# 	Boolean indicating if the operation was
	# 	successful or not.
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
	# Adds a new element in a given position of the list.
	# Parameters:
	# 	pos  - position in the list.
	# 	elem - new element.
	# Returns:
	# 	Boolean indicating if the operation was
	# 	successful or not.
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
	# Remove the given element from the list.
	# Parameters:
	# 	elem - element to be removed.
	# Returns:
	# 	Boolean indicating if the operation was
	# 	successful or not.
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
	# Removes the element in the given position.
	# Parameters:
	# 	pos - position in the list to be removed.
	# Returns:
	# 	Boolean indicating if the operation was
	# 	successful or not.
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
	# Returns the position of the given element.
	# Parameters:
	# 	elem - element to be found.
	# Returns:
	# 	Position of the given element, or -1 if the 
	#	is not found in the list.
	def index_of(self, elem):
		node, i = self.__head, 0
		while node != None:
			if(node.get_value() == elem):
				return i
			node = node.get_next()
			i += 1
		return -1

	# elem_at(self, pos)
	# Returns the element found on a given position.
	# Parameters:
	# 	pos - position in the list.
	# Returns:
	# 	Element found in the given position, or None if the
	#	if the position goes out of bounds.
	def elem_at(self, pos):
		if pos < 0 or pos >= self.__size:
			return None
		node = self.__head
		for _ in range(pos):
			node = node.get_next()
		return node.get_value()

	# contains(self, elem)
	# Verifies if an element is found in the list.
	# Parameters:
	# 	elem - element to be looked for.
	# Returns:
	# 	Boolean indicating if it is found or not in the list.
	def contains(self, elem):
		return self.index_of(elem) > -1

	# size(self)
	# Returns the size of the list.
	# Returns:
	# 	List size.
	def size(self):
		return self.__size

	# empty(self)
	# Removes all the elements from the list.
	def empty(self):
		while self.__head != None:
			self.remove_from(0)

	# to_array(self)
	# Returns an array list of the elements of the linked list.
	# Returns:
	# 	Array list with the elements.
	def to_array(self):
		array = []
		for elem in self:
			array.append(str(elem))
		return array



