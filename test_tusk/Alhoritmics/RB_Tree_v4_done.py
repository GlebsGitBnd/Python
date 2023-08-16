# Инициализатор узла
class Node:
	def __init__(self, data):
		self.data = data
		self.left = self.right = self.parent = self.link = None
		self.color = 'RED'


# Класс дерева
class RBTree:
	def __init__(self):
		self.nil = Node(None)
		self.nil.color = 'BLACK'
		self.root = self.nil
	
	# Поиск Ветки
	def find(self, node_value, parent, current):
		if current.data is None:
			return parent, False
		elif node_value is current.data:
			return current, True
		elif node_value < current.data:
			if current.left:
				return self.find(node_value, current, current.left)
		elif node_value > current.data:
			if current.right:
				return self.find(node_value, current, current.right)
	
	# Добавление элемента в ветку
	def append(self, data):
		node = Node(data)
		print('ДОБАВЛЯЕМ', node.data)
		
		if self.root is self.nil:
			node.color = 'BLACK'
			self.root = node
			node.left = node.right = self.nil
			return
		
		dad, presence = self.find(node.data, None,
		                          self.root)  # Проверяем есть ли элемент в дереве, ищем родителя
		
		if not presence:  # Добавляем элемент если его нет
			if dad.data > node.data:  # Делаем соединение назначаем родителя
				dad.left = node  # ПРОБУЕМ ПОД ЗАМЕНУ
				node.parent = dad
				node.relation = 'left'
			else:
				dad.right = node
				node.parent = dad
				node.relation = 'right'
			node.left = node.right = self.nil
		
		print()
		self.tree_show(self.root)
		print()
		
		self.to_fixed(node, dad)
	
	# Фиксация баланса дерева
	def to_fixed(self, node, dad):
		if node is self.root:
			return
		print(node.data, node.color, dad.data, dad.color, 'до')
		if node.color == 'RED' and dad.color == 'RED':
			grand_dad = node.parent.parent
			uncle = grand_dad.left if dad is grand_dad.right else grand_dad.right
			if uncle.color == 'BLACK':
				node, dad = self.to_low_rotate(node, dad,
				                               grand_dad)  # На этом моменту нода становится отцом
				print(node.data, dad.data, grand_dad.data)
				self.to_big_rotate(dad, grand_dad, False)
			elif uncle.color == 'RED':
				dad.color = uncle.color = 'BLACK'
				grand_dad.color = 'RED'
				print()
				print('Перекрас')
				self.tree_show(self.root)
				print()
			self.root.color = 'BLACK'
			print(node.data, node.color, dad.data, dad.color, 'после')
		self.to_fixed(node.parent, node.parent.parent)
	
	# Малый поворот
	def to_low_rotate(self, node, dad, grand_dad):
		if node is dad.right and dad is grand_dad.left:
			dad.right, dad.right.parent, dad.parent = node.left, dad, node
			node.left, node.parent = dad, grand_dad
			grand_dad.left = node
			print('Сейчас будет лоу ротате')
			self.tree_show(self.root)
			print()
			return dad, node
		elif node is dad.left and dad is grand_dad.right:
			dad.left, dad.left.parent, dad.parent = node.right, dad, node
			node.right, node.parent = dad, grand_dad
			grand_dad.right = node
			print('Сейчас будет лоу ротате')
			self.tree_show(self.root)
			print()
			return dad, node
		print('Сейчас будет лоу ротате')
		self.tree_show(self.root)
		print()
		return node, dad
	
	# Большой поворот
	def to_big_rotate(self, dad, grand_dad, delete):
		print('\nСейчас будет биг ротате')
		if grand_dad is self.root:
			self.root = dad
			self.root.parent = None
		else:
			if grand_dad.parent.data > dad.data:
				grand_dad.parent.left = dad
			else:
				grand_dad.parent.right = dad
			dad.parent = grand_dad.parent
		
		if grand_dad.data > dad.data:
			grand_dad.left, dad.right.parent = dad.right, grand_dad
			dad.right = grand_dad
		else:
			grand_dad.right, dad.left.parent = dad.left, grand_dad
			dad.left = grand_dad
		grand_dad.parent = dad
		
		if not delete:
			grand_dad.color, dad.color = 'RED', 'BLACK'
		self.root.color = 'BLACK'
		print()
		self.tree_show(self.root)
		print()
	
	# Удаление ноды
	def delete_node(self, num):
		node, exist = self.find(num, None, self.root)
		print('УДАЛЯЕМ', node.data)
		
		if not exist:
			print(f'Значение {node.data} отсутствует')
			return
		
		left_son, right_son = node.left, node.right
		dad = node.parent
		if left_son.data and right_son.data:  # Если 2 ребенка
			print('two child')
			last_elem = self.del_node_with_two(right_son)
			print(last_elem.data, 'dfsfsdfsdf')
			elem = self.delete_node(last_elem.data)
			
			last_elem = elem if last_elem.right else last_elem
			print('doshlo')
			node.data, last_elem.data = last_elem.data, node.data
			
			self.tree_show(self.root)
			print()
		
		if (left_son.data and not right_son.data) \
			or (right_son.data and not left_son.data):  # Если 1 ребенок
			print('one child')
			present_son = left_son if left_son.data else right_son
			print(present_son.data, 'ячсячсячсячс')
			self.delete_node(present_son.data)
			node.data, present_son.data = present_son.data, node.data
			
			self.tree_show(self.root)
			print()
			
			return present_son
		
		if not right_son.data and not right_son.data:  # Если нет детей
			print('no child')
			self.del_node_without_child(node, dad)
			self.tree_show(self.root)
			print()
		print('Вернуло')
		return self.tree_show(self.root)
	
	# Нахождение минимального числа для свапа (При удалении когда 2 сына)
	def del_node_with_two(self, last_elem):
		if last_elem.left.data is None:
			return last_elem
		return self.del_node_with_two(last_elem.left)
	
	# Удаление когда нет детей
	def del_node_without_child(self, node, dad):
		if node.color == 'RED':
			print('del', node.data, 'red')
			self.link_removal_node(node, dad)
		elif node.color == 'BLACK':
			print('del', node.data, 'black')
			self.del_node_without_child_black(node, dad)
			self.link_removal_node(node, dad)
	
	def del_node_without_child_black(self, node, dad):
		if node is self.root:
			return
		
		if node is node.parent.left:
			print('left side')
			self.choose_side('left', node, dad)
		else:
			print('right side')
			self.choose_side('left', node, dad)
	
	def choose_side(self, side, node, dad):
		sibling = dad.right if node is dad.left else dad.left
		lft_gr_son, rht_gr_son = sibling.left, sibling.right
		print(node.data, node.color, sibling.data, sibling.color)
		
		if side == 'right':
			lft_gr_son, rht_gr_son = rht_gr_son, lft_gr_son
		
		print(node.data, node.color, sibling.data, node.parent.data, 'sib')
		print()
		self.tree_show(self.root)
		
		if sibling.color == 'BLACK':
			if rht_gr_son.color == 'RED':
				print('1.1 a)')
				self.sib_black_rht_gr_son_red(sibling, dad, rht_gr_son)
			
			elif lft_gr_son.color == 'RED':
				print('1.1 б)')
				self.sib_black_lft_gr_son_red(sibling, lft_gr_son)
				print('1.1 a)')
				self.sib_black_rht_gr_son_red(lft_gr_son, dad, sibling)
			
			elif lft_gr_son.color == 'BLACK' and rht_gr_son.color == 'BLACK':
				print('1.2')
				sibling.color = 'RED'
				
				self.recursion_balance_black(node, dad)
				self.tree_show(self.root)
				print()
		elif sibling.color == 'RED':
			self.to_big_rotate(sibling, dad, True)
			sibling.color = 'BLACK'
			dad.color = 'RED'
			self.del_node_without_child_black(node, node.parent)
			self.tree_show(self.root)
			print()
	
	def recursion_balance_black(self, node, dad):
		if dad.color == 'RED':
			print('dad red')
			dad.color = 'BLACK'
			print('удаление завершено')
		else:
			print('dad black')
			root = self.root
			while root is self.root and node is not dad:
				node = node.parent
				self.del_node_without_child_black(node, node.parent)
				print('конец')
			print('удаление завершено')
	
	def sib_black_rht_gr_son_red(self, sibling, dad, gr_son):  # 1.1 a)
		self.to_big_rotate(sibling, dad, True)
		sibling.color = dad.color
		dad.color = gr_son.color = 'BLACK'
		print(sibling.data, sibling.color)
	
	def sib_black_lft_gr_son_red(self, sibling, gr_son):  # 1.1 б)
		self.to_big_rotate(gr_son, sibling, True)
		sibling.color, gr_son.color = 'RED', 'BLACK'
		print(sibling.data, sibling.color)
	
	def link_removal_node(self, node, dad):
		if node is dad.left:
			dad.left = self.nil
		else:
			dad.right = self.nil
		node.left = node.right = node.parent = None
	
	def tree_show(self, node):
		left_brother, right_brother, parent = node.left, node.right, node.parent
		if node.data is None:
			return
		self.tree_show(left_brother)
		parent_data = parent.data if parent else parent
		print(
			f'data:{node.data}, parent:{parent_data}, color:{node.color}, '
			f'left:{left_brother.data}, right:{right_brother.data}')
		self.tree_show(right_brother)


def main(lst):
	tree = RBTree()
	for i in lst:
		tree.append(i)
	print('----------DELETE------------------')
	tree.delete_node(160)
	print('----------DELETE------------------')
	tree.delete_node(180)
	print('----------DELETE------------------')
	tree.delete_node(220)
	print('----------DELETE------------------')
	tree.delete_node(240)
	print('----------DELETE------------------')
	tree.delete_node(260)
	print('----------DELETE------------------')
	tree.delete_node(280)
	print('----------DELETE------------------')
	tree.delete_node(300)
	print('----------DELETE------------------')
	tree.delete_node(320)
	print('----------DELETE------------------')
	tree.delete_node(320)


# main([20, 25, 8, 23, 4, 16, 30, 10, 2, 17, 5, 19, 3, 12, 9, 13])                  #1.1 а)left Правый ребенок брата красный (левый -- любой)  del 9
# main([20, 25, 8, 23, 4, 16, 30, 10, 2, 17, 5, 19, 3, 12, 9, 11])                  #1.1 б)left Правый ребенок брата красный (левый -- любой)  del 9
# main([20, 25, 8, 23, 4, 16, 30, 10, 2, 17, 5, 19, 3, 12, 9, 11])                  #1.2 а)left Правый ребенок брата красный (левый -- любой)  del 3 del 2
main(
	[100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380,
	 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600])

