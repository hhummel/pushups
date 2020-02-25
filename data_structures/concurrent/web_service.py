import time, threading, queue, random

class Item():
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Item message: {self.message}"

class Service():
    
    def __init__(self, num_threads=2):
        self.queue = queue.Queue()
        self.num_threads = num_threads
        self.threads = []
        self.start_queue()

    def do_task_A(self, item, sec=2):
        print(f"do_task received message: {item.message} queue size: {self.queue.qsize()}")
        print(f"do_task sleep: {sec}")
        time.sleep(sec)
        num = random.random()
        if 0 < num <= 0.3:
            self.queue.put(Item("B"))
        elif 0.3 < num < 0.7:
            self.queue.put(Item("C"))
        else:
            print("Done")

    def do_task_B(self, item, sec=2):
        print(f"do_task received message: {item.message} queue size: {self.queue.qsize()}")
        print(f"do_task sleep: {sec}")
        time.sleep(sec)
        num = random.random()
        if 0 < num <= 0.3:
            self.queue.put(Item("C"))
        elif 0.3 < num < 0.7:
            self.queue.put(Item("A"))
        else:
            print("Done")

    def do_task_C(self, item, sec=2):
        print(f"do_task received message: {item.message} queue size: {self.queue.qsize()}")
        print(f"do_task sleep: {sec}")
        time.sleep(sec)
        num = random.random()
        if 0 < num <= 0.3:
            self.queue.put(Item("B"))
        elif 0.3 < num < 0.7:
            self.queue.put(Item("A"))
        else:
            print("Done")

    def worker(self):
        while True:
            item = self.queue.get()
            if item.message == "A":
                self.do_task_A(item)
            elif item.message == "B":
                self.do_task_B(item)
            elif item.message == "C":
                self.do_task_C(item)
            self.queue.task_done()

            if item.message == None:
                print("None item, so break")
                break
            
    def start_queue(self):
        for i in range(self.num_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            self.threads.append(t)

    def stop_queue(self):
        for i in range(self.num_threads):
            self.submit(None)
        
    def submit(self, message):
        self.queue.put(Item(message))
        #self.queue.join()
