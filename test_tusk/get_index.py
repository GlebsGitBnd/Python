from random import randint


lst = [randint(1, 8) for i in range(10)]


def get_index(lst, num):
	for i, j in enumerate(lst):
		for x, y in enumerate(lst[i+1:]):
			if j + y == num:
				return i, x + (i+1)


print(lst)
print(get_index(lst, 15))