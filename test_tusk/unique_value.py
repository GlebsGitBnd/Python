# from random import randint
#
#
# lst = [randint(1, 8) for i in range(10)]
#
#
# def get_unique(arg):
# 	cash = []
# 	for i in range(len(arg)):
# 		count = 0
# 		if arg[i] in cash:
# 			count += 1
# 			continue
# 		for j in arg[i+1:]:
# 			if arg[i] == j:
# 				count += 1
# 				cash.append(arg[i])
# 				break
# 		if count == 0:
# 			return arg[i]
# 	return 'Уникальных значений нет'
#
#
# print(lst)
# print(get_unique(lst))

from random import randint


lst = [randint(1, 8) for i in range(10)]


def get_unique(arg):
	for i in arg:
		if arg.count(i) == 1:
			return i
	return 'Уникальных значений нет'


print(lst)
print(get_unique(lst))



