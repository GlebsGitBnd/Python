from threading import Thread, Lock
import time


class Queue:
	def __init__(self):
		self.items = []
	
	def put(self, item):
		self.items.append(item)
	
	def get(self):
		return self.items.pop(0)
	
	def size(self):
		return len(self.items)
	
	def isEmpty(self):
		return self.size() == 0
	
	def peek(self):
		return self.items[0]


class ThreadSaifQueue(Queue):
	# Реализация потокобезопасной очереди
	def __init__(self):
		super().__init__()
		self.lock = LockApply()
		
	def queue_start(self):
		while True:
			self.queue_check()
	
	def queue_check(self):
		if not self.isEmpty():
			with self.lock.use_lock():
				current_tusk = self.get()
				use_tusk = TuskUse(current_tusk)
				print(use_tusk.use_work())


class LockApply:
	def __init__(self):
		self.lock = Lock()
	
	def use_lock(self):
		return self.lock


class TuskUse:
	def __init__(self, tusk):
		self.tusk = tusk
		
	def use_work(self):
		return self.tusk.work()
	
	
class Work:
	def __init__(self, value):
		self.value = value
	
	def work(self):
		# Имиитация полезной работы
		time.sleep(5)
		return self.value * 2


class WorkProduce:
	def __init__(self, clazz):
		self.clazz = clazz
	
	def produce(self, value):
		return self.clazz(value)
# Задача: реализовать неблокирующий ввод задач и обработку их в потоке демоне


def main():
	queue_1 = ThreadSaifQueue()
	produce = WorkProduce(Work)
	daemon_thread = Thread(target=queue_1.queue_start, daemon=True)
	daemon_thread.start()
	while True:
		num = int(input())
		work = produce.produce(num)
		queue_1.put(work)


if __name__ == '__main__':
	main()
	