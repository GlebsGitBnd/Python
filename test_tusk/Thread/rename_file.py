# import os
#
#
# def rename_file(directory, prefix):
# 	for file_name in os.listdir(directory):
# 		new_path = os.path.join(directory, file_name)
# 		# current_path = new_path.rstrip(file_name) + prefix + file_name
# 		current_path = new_path.replace(prefix, '')    # Удаление префикса
# 		os.rename(new_path, current_path)
# 		if not os.path.isfile(current_path):
# 			rename_file(current_path, prefix)
#
#
# pathh = r'C:\Users\Admin\Desktop\test'
# prefix = 'py_pre_'
#
# rename_file(pathh, prefix)



##############################################################################
##############################################################################

from os import listdir, rename, path
from time import time
from threading import Thread


def timer(fn):
	def wrapper(*args, **kwargs):
		start = time()
		print('Начало')
		fn(*args, **kwargs)
		end = time()
		print(f'Время работы функции {end - start}')
	return wrapper


def rename_file(directory, prefix):
	for file_name in listdir(directory):
		new_path = path.join(directory, file_name)
		current_path = new_path.rstrip(file_name) + prefix + file_name
		# current_path = new_path.replace(prefix, '')    # Удаление префикса
		rename(new_path, current_path)
		if not path.isfile(current_path):
			tread = Thread(target=rename_file, args=(current_path, prefix,))
			tread.start()


@timer
def main():
	rename_file(pathh, prefix)


pathh = r'C:\Users\Admin\Desktop\test'
prefix = 'py_pre_'
main()

##############################################################################
##############################################################################

# import asyncio
# from os import listdir, rename, path
#
#
# async def rename_file(directory, prefix):
# 	for file_name in listdir(directory):
# 		new_path = path.join(directory, file_name)
# 		# current_path = new_path.rstrip(file_name) + prefix + file_name
# 		current_path = new_path.replace(prefix, '')    # Удаление префикса
# 		rename(new_path, current_path)
# 		if not path.isfile(current_path):
# 			await rename_file(current_path, prefix)
#
#
# pathh = r'C:\Users\Admin\Desktop\test'
# prefix = 'py_pre_'
#
#
# async def main():
# 	await rename_file(pathh, prefix)
#
#
# asyncio.run(main())
