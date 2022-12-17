import unittest

class Stack:
    def __init__(self):
        self.items = []
        self.on_list = {}	

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def push(self, item):
        if not item in self.on_list:
            self.on_list[item] = 1
            self.items.append(item)

    def pop(self):
        res = self.items.pop()
        self.on_list.pop(res)
        return res

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stk = Stack()
        for item in [2, 3, 4, 5, 6]:
            self.stk.push(item)

    def testPush(self):
        self.stk.push(2)
        self.assertEqual(str(self.stk), str(self.stk))
        self.stk.push(7)
        self.assertEqual(str(self.stk), "[2, 3, 4, 5, 6, 7]")

    def testPop(self):
        self.assertEqual(self.stk.pop(), 6)


if __name__ == '__main__':
    unittest.main()