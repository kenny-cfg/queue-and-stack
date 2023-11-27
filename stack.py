class Stack:
    def __init__(self, *args):
        self.storage = []
        for arg in args:
            self.storage.append(arg)

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        value = self.storage[-1]
        self.storage = self.storage[0:-1:]
        return value
