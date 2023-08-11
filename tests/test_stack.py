"""Module that contains Stack UnitTests"""
import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    """Unit Tests Class for Stack class"""

    def test_get_when_empty(self):
        """Test popping a single item to the stack when it is empty"""
        stk = Stack()
        self.assertRaises(ValueError, stk.pop)

    def test_add_single_item(self):
        """Test adding single  item to the stack"""
        stk = Stack()
        stk.push(1)
        self.assertEqual(stk.pop(), 1)

    def test_add_multiple_items_int(self):
        """Test adding multiple int items to the stack"""
        stk = Stack()
        stk.push(1)
        stk.push(2)
        stk.push(3)
        self.assertEqual(stk.pop(), 3)
        self.assertEqual(stk.pop(), 2)
        self.assertEqual(stk.pop(), 1)
        self.assertRaises(ValueError, stk.pop)

    def test_add_multiple_items_string(self):
        """Test adding multiple string items to the stack"""
        stk = Stack()
        stk.push("a")
        stk.push("b")
        stk.push("c")
        self.assertEqual(stk.pop(), "c")
        self.assertEqual(stk.pop(), "b")
        self.assertEqual(stk.pop(), "a")
        self.assertRaises(ValueError, stk.pop)
