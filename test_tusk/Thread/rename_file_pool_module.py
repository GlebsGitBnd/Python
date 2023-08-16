from concurrent.futures import ThreadPoolExecutor
from os import listdir, rename, path
from time import time


def timer(fn):
	def wrapper(*args, **kwargs):
		start = time()
		print('Начало')
		fn(*args, **kwargs)
		end = time()
		print(f'Время работы функции {end - start}')
	return wrapper


def rename_file(directory, prefix, e):
	for file_name in listdir(directory):
		new_path = path.join(directory, file_name)
		# current_path = new_path.rstrip(file_name) + prefix + file_name
		current_path = new_path.replace(prefix, '')    # Удаление префикса
		rename(new_path, current_path)
		if not path.isfile(current_path):
			e.submit(rename_file, directory, prefix)
			# tread = Thread(target=rename_file, args=(current_path, prefix,))


@timer
def main():
	with ThreadPoolExecutor(max_workers=1) as e:
		rename_file(pathh, prefix, e)


pathh = r'C:\Users\Admin\Desktop\test'
prefix = 'py_pre_'
main()
