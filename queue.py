# Queue, i.e. FIFO object

class Queue:
    def __init__(self):
        self.storage = []

    def push(self, element):
        self.storage.append(element)

    def pop(self):
        value = self.storage[0]
        self.storage = self.storage[1::]
        return value
