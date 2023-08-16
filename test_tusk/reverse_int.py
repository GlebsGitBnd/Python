from sys import maxsize


def get_revers(num):
	s = str(num)
	return 0 if int(s[::-1]) > maxsize else int(s[::-1])


print(get_revers(123412341234123423))