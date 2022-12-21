import random

class RandomQueue:

    def __init__(self, max_size=10):
        self.q = [None] * max_size
        self.max_size = max_size
        self.size = 0
    
    @property
    def prev_index(self):
        return self.size - 1

    def insert(self, item):   # wstawia element w czasie O(1)
        if self.is_full():
            raise ValueError("kolejka pelna")
        
        self.q[self.size] = item
        self.size = self.size + 1

    def remove(self):   # zwraca losowy element w czasie O(1)
        if not self.is_empty():
            i = random.randint(0, self.prev_index)
            item = self.q[i]

            if i == self.prev_index:
                self.q[i] = None
            else:
                self.q[i] = self.q[self.prev_index]
                self.q[self.prev_index] = None

            self.size = self.size - 1
            return item
        else:
            raise ValueError("kolejka pusta")

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def clear(self):   # czyszczenie listy
        self.q = [None] * self.max_size
        self.size = 0