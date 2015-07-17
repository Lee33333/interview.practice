class Node:
	def __init__(self, value): 
		#self.root = None
		self.right = None
		self.left = None
		self.value = value


class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def append_node(self, value):
		new_node = Node(value)
		#initialize the node then append to the tree
		
		#when you initialize it
		if self.root == None:
			#if there's no root (e.g., this is the first node), set root to new node
			self.root = new_node

		else:
			#start search at root
			#"node" is a marker for where we currently are
			node = self.root
			while node:
				if (new_node.value < node.value) and node.left:
					node = node.left
				#so if there isn't a node to the left
				elif new_node.value < node.value:
					node.left = new_node
				if (new_node.value > node.value) and node.right:
					#checks if node to right exists, move right --> new root
					node = node.right
				#so if there isn't a node to the right
				elif new_node.value > node.value:
					#set node.right to new_node (add to tree)
					node.right = new_node
				if new_node.value == node.value:
					break

# breadth first search
def BFT(node):
	q = []
	if node:
		q.append(node)
	while q:
		print q[0].value
		#you could also type print node.value
		#or print q[0].value
		node = q.pop(0)
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)


#3 types of depth first
def in_order(node):
	if node:
		in_order(node.left)
		print node.value
		in_order(node.right)


def pre_order(node):
	if node:
		print node.value
		in_order(node.left)
		in_order(node.right)

def post_order(node):
	if node:
		in_order(node.left)
		in_order(node.right)
		print node.value

