lst = [23, 1, 2, 4, 3, 78, 4, 5, 7, 3, 54, 67, 78, 23, 123]


def bubble_sort(lst):
	for i in range(len(lst)-1):
		for j in range(len(lst) - 1 - i):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
	return lst


def check_positive(lst):
	for i in range(len(lst)):
		if lst[i] > 1 and i == 0:
			return lst[i] - 1
		elif (lst[i+1] - lst[i]) > 1:
			return lst[i] + 1


new_lst = bubble_sort(lst)
print(lst)
print(check_positive(new_lst))
