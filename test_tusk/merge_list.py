from operator import itemgetter


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


def bubble_sort(lst):
	for i in range(len(lst)-1):
		for j in range(len(lst) - 1 - i):
			if lst[j][0] > lst[j + 1][0]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
	return lst


def sort_list(head: Node):
	lst = []
	head_sort = Node()
	current = head_sort
	while head:
		lst.append([head.getValue(), head])
		head = head.getNext()
	lst = bubble_sort(lst)
	print(lst)
	while lst:
		current.setNext(lst.pop(0)[1])
		current = current.getNext()
	current.setNext(None)
	return head_sort.getNext()


def merge_list(head1: Node, head2: Node):
	head_merge = Node()
	current = head_merge
	head1 = sort_list(head1)
	head2 = sort_list(head2)
	while head1 or head2:
		if not head2 or (head1.getValue() <= head2.getValue()):
			current.setNext(head1)
			head1 = head1.getNext()
		else:
			current.setNext(head2)
			head2 = head2.getNext()
		current = current.getNext()
	return head_merge.getNext()


node_first_1 = Node(10)
node_first_2 = Node(20)
node_first_3 = Node(1)
node_first_4 = Node(5)

node_first_1.setNext(node_first_2)
node_first_2.setNext(node_first_3)
node_first_3.setNext(node_first_4)

node_second_1 = Node(2)
node_second_2 = Node(6)
node_second_3 = Node(4)

node_second_1.setNext(node_second_2)
node_second_2.setNext(node_second_3)


new_merge = merge_list(node_first_1, node_second_1)
while new_merge:
	print(new_merge.getValue(), end=' ')
	new_merge = new_merge.getNext()