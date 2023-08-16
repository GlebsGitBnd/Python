from threading import Thread
import queue
from time import sleep


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
            print(task.work())
    
    def start(self):
        for i in range(self.max_threads):
            thread = Thread(target=self.worker_thread)
            thread.start()
    
    def submit(self, work):
        for i in work:
            produce = WorkProduce(Work)
            task = produce.produce(i)
            self.queue.put(task)
        

class Work:
    def __init__(self, value):
        self.value = value
    
    def work(self):
        # Имиитация полезной работы
        sleep(5)
        return self.value * 2


class WorkProduce:
    def __init__(self, clazz):
        self.clazz = clazz
    
    def produce(self, value):
        return self.clazz(value)


def main():
    thread = ThreadPool(3)
    thread.start()
    while True:
        data = list(map(int, input('Введите числа через пробел:').split(' ')))
        thread.submit(data)
        print(data)


if __name__ == '__main__':
    main()
    