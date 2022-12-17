from collections import deque
import random
import unittest

class RandomQueue:

    def __init__(self):
        self.items = deque()
        self.size = 0

    def insert(self, item):   # wstawia element w czasie O(1)
        head_or_tail = random.randint(0, 1)

        if head_or_tail == 1:
            self.items.append(item);
        else:
            self.items.appendleft(item)
        
        self.size = self.size + 1

    def remove(self):   # zwraca losowy element w czasie O(1)
        if not self.is_empty():
            head_or_tail = random.randint(0, 1)
            self.size = self.size - 1
            if head_or_tail == 1:
                return self.items.pop()
            else:
                return self.items.popleft()
        else:
            raise ValueError("kolejka pusta")

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return False

    def clear(self): pass   # czyszczenie listy

class RandomQueueTest(unittest.TestCase):
    def setUp(self):
        self.rq0 = RandomQueue()
        self.rq1 = RandomQueue()
        for item in [1, 2, 3, 4]:
            self.rq1.insert(item)

    def testRemove(self):
        self.assertEqual(self.rq1.remove() in [1, 2, 3, 4], True)
        with self.assertRaises(QueueEmpty):
            self.rq0.remove()


if __name__ == '__main__':
    unittest.main()	



'''def __init__(self, max_size):
    self.max_size = max_size
    self.queue = []

def insert(self, item):
    if len(self.queue) < self.max_size:
        self.queue.append(item)
    else:
        print("Queue is full")

def remove(self):
    if len(self.queue) > 0:
        index = random.randrange(0, len(self.queue))
        item = self.queue[index]
        del self.queue[index]
        return item
    else:
        print("Queue is empty")

def is_empty(self):
    return len(self.queue) == 0

def is_full(self):
    return len(self.queue) == self.max_size

def clear(self):
    self.queue = []
'''