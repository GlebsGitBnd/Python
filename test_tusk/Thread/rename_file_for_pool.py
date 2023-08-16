from threading import Thread
from os import listdir, rename, path
from functools import partial
import queue
from time import time


class ThreadPool:
	# Реализация пула потоков для обработки задач
	def __init__(self, max_threads):
		self.max_threads = max_threads
		self.queue = queue.Queue()
	
	def worker_thread(self):
		while True:
			task = self.queue.get()
			if task is None:
				break
			task()
	
	def start(self):
		for i in range(self.max_threads):
			thread = Thread(target=self.worker_thread)
			thread.start()
	
	def wait_completion(self):
		self.queue.join()
		for _ in range(self.max_threads):
			self.queue.put(None)
			
	def submit(self, work):
		self.queue.put(work)


class File:
	def __init__(self, pool):
		self.pool = pool
		
	def rename_file(self, directory, prefix):
		for file_name in listdir(directory):
			new_path = path.join(directory, file_name)
			current_path = new_path.rstrip(file_name) + prefix + file_name
			# current_path = new_path.replace(prefix, '')  # Удаление префикса
			rename(new_path, current_path)
			if not path.isfile(current_path):
				self.pool.submit(partial(self.rename_file, current_path, prefix))


def timer(fn):
	def wrapper(*args, **kwargs):
		start = time()
		print('Начало')
		fn(*args, **kwargs)
		end = time()
		print(f'Время работы функции {end - start}')
	return wrapper


pathh = r'C:\Users\Admin\Desktop\test'
prefix = 'py_pre_'


@timer
def main():
	thread = ThreadPool(1)
	thread.start()
	file = File(thread)
	file.rename_file(pathh, prefix)


if __name__ == '__main__':
	main()