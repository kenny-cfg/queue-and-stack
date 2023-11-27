# Queue, i.e. FIFO object

class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, element):
        self.storage.append(element)

    def dequeue(self):
        value = self.storage[0]
        self.storage = self.storage[1::]
        return value
