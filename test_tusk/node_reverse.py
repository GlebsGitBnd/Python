class Node:
	__value: int
	__next: "Node"
	
	def __init__(self, value=None, next=None):
		self.__value = value
		self.__next = next
	
	def getValue(self):
		return self.__value
	
	def setValue(self, value):
		self.__value = value
	
	def getNext(self):
		return self.__next
	
	def setNext(self, next):
		self.__next = next
		

def node_reverse(head: Node, k: int):
	head_reverse = Node()
	current = head_reverse
	nodes = []
	count = 0
	while head or len(nodes):
		if head and len(nodes) < k:
			nodes.append(head)
			head = head.getNext()
			count += 1
		else:
			while nodes:
				last = nodes.pop() if count == k else nodes.pop(0)
				current.setNext(last)
				current = current.getNext()
			count = 0
	current.setNext(None)
	return head_reverse.getNext()
	

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.setNext(node2)
node2.setNext(node3)
node3.setNext(node4)
node4.setNext(node5)


revers = node_reverse(node1, 3)
while revers:
	print(revers.getValue(), end=' ')
	revers = revers.getNext()