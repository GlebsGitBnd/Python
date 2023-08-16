import time
from typing import Union


def cash_decor(fn):
	cash = {}
	
	def wrapper(arg):
		if arg in cash:
			return cash[arg]
		else:
			cash[arg] = fn(arg)
		return cash[arg]
	return wrapper


@cash_decor
def get_square_number(num: Union[int, float]):
	time.sleep(3)
	return num**2


print(get_square_number(10))
print(get_square_number(20))
print(get_square_number(10))