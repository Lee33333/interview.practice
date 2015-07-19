# Write a linked list implementation with methods that do these things:
# - get node by index!
# - get index of node!
# - add node at index!
# - delete node at index!
# - returns length of list!
# - print list!
# Bonus:
# - methods to find min and max of list

class Node:
	def __init__(self, value):
		self.next = None
		self.value = value

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return str(self.value)

class List:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def get_length(self):
		return self.size

	def print_list(self):
		current_node = self.head
		while current_node:
			print current_node.value
			current_node = current_node.next

	def print_node_value(self, index):
		node = self.get_node_by_index(index)
		print node.value

	def get_node_by_index(self, index):

		if int(index) < self.size:
			position = 0
			current_node = self.head

			while current_node:
				if position == int(index):
					return current_node
				position = position + 1
				current_node = current_node.next
		else:
			print "Your index is longer than the list"


	def add_node(self, value):

		new_node = Node(str(value))

		if not self.head:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

		self.size = self.size + 1

	def delete_node_by_index(self, index):
		# not re-setting tail, why?
		if int(index) <= self.size -1:
			self.size = self.size -1

			if index == 0:

				if self.size == 0:
					self.head = None
					self.tail = None

				else:
					temp = self.head
					self.head = temp.next

			elif index == self.size-1:
				previous_index = int(index) -1
				previous_node = self.get_node_by_index(previous_index)

				previous_node.next = None
				self.tail = previous_node

			else:
				previous_index = int(index) -1
				previous_node = self.get_node_by_index(previous_index)

				temp = previous_node.next.next
				previous_node.next = temp
		else:
			print "Your index your index is out of range"

	def add_node_by_index(self, value, index):
		# not re-setting tail, why?
		
		if index <+ self.size + 1:
			new_node = Node(value)
			self.size = self.size + 1

			if index == 0:
				new_node.next = self.head
				self.head = new_node
				

			elif index < self.size:
				previous_index = int(index) -1
				previous_node = self.get_node_by_index(previous_index)

				new_node.next = previous_node.next
				previous_node.next = new_node

			else:
				self.tail.next = new_node
				self.tail = new_node

		else:
			print "Your index your index is out of range"

	def get_node_by_value(self, value):
		current_node = self.head
		counter = 0
		while current_node.value != value:
			if not current_node.next:
	 			return "Cannot find this value"
	 		current_node = current_node.next
	 		counter = counter + 1
	 	return counter


