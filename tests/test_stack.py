import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_get_when_empty(self):
        s = Stack()
        self.assertRaises(ValueError, s.pop)

    def test_add_single_item(self):
        s = Stack()
        s.push(1)
        self.assertEquals(s.pop(), 1)

    def test_add_multiple_items(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEquals(s.pop(), 3)
        self.assertEquals(s.pop(), 2)
        self.assertEquals(s.pop(), 1)
        self.assertRaises(ValueError, s.pop)
