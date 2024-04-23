# třída spojení datových struktur jako fronta

class CharQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            return True
        return False

    def dequeue(self): #vrátí první prvek
        if not self.is_empty():
            item = self.queue.pop(0) # pop s indegem vrátí první prvek 0 pokud nedám 0 vrátí poslední
            return item
        return None

    def show(self):
        if not self.is_empty():
            pass




