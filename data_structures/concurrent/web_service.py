import time, threading, queue, random

class Item():
    def __init__(self, message, key=None):
        self.message = message
        self.key = key
        self.history = []

    def __str__(self):
        return f"Item message: {self.message}"

class Service():
    
    def __init__(self, num_threads=2):
        self.queue = queue.Queue()
        self.num_threads = num_threads
        self.threads = []
        self.start_queue()
        self.key = 1
        self.choices = {
            "A": ["B", "C", None],
            "B": ["C", "A", None],
            "C": ["A", "B", None],
        }

    def do_task(self, label, item, sec=2):
        print(f"do_task received message: {item.message} id: {item.key} queue size: {self.queue.qsize()}")
        print(f"do_task sleep: {sec}")
        time.sleep(sec)
        choice = random.choice(self.choices[label])
        if choice:
            item.message = choice
            item.history.append(choice)
            self.submit_item(item)
        else:
            print(f"Done id: {item.key} history: {item.history}")

    def do_task_A(self, item):
        self.do_task("A", item)

    def do_task_B(self, item, sec=2):
        self.do_task("B", item)

    def do_task_C(self, item, sec=2):
        self.do_task("C", item)

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
        item = Item(message, self.key)
        self.key += 1
        item.history.append(message)
        self.queue.put(item)
        
    def submit_item(self, item):
        self.queue.put(item)
