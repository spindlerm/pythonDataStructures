"""Module that contains LinkedList UnitTests"""
import io
import unittest
from contextlib import redirect_stdout

from linked_list import LinkedList


class TestStack(unittest.TestCase):
    """Unit Tests Class for Stack class"""

    def test_is_empty_when_empty(self):
        l_l = LinkedList()
        self.assertEqual(True, l_l.is_empty())

    def test_is_empty_when_not_empty(self):
        """ "Test empty() on non empty list empty list"""
        l_l = LinkedList()
        l_l.add_tail(1)
        self.assertEqual(False, l_l.is_empty())

    def test_get_head_when_empty(self):
        """ "Test getting head item from empty list"""
        l_l = LinkedList()
        self.assertRaises(ValueError, l_l.get_head)

    def test_tail_head_when_empty(self):
        """ "Test getting tail item from empty list"""
        l_l = LinkedList()
        self.assertRaises(ValueError, l_l.get_tail)

    def test_add_one_item(self):
        """ "Test adding one item to the tail of the list"""
        l_l = LinkedList()
        l_l.add_tail(1)
        self.assertEqual(l_l.get_tail(), 1)

    def test_add_multiple_items(self):
        """ "Test adding multiple items to the tail of the list"""

        l_l = LinkedList()
        l_l.add_tail("a")
        l_l.add_tail("b")
        l_l.add_tail("c")
        self.assertEqual(l_l.get_head(), "a")
        self.assertEqual(l_l.get_tail(), "c")

    def test_pop_head(self):
        """ "Test pop of an item from head of list"""

        l_l = LinkedList()
        l_l.add_tail(1)
        l_l.add_tail(2)
        l_l.add_tail(3)
        self.assertEqual(l_l.pop_head(), 1)
        self.assertEqual(l_l.pop_head(), 2)
        self.assertEqual(l_l.pop_head(), 3)
        self.assertEqual(l_l.is_empty(), True)

    def test_pop_tail(self):
        """ "Test pop of an item from tail of list"""

        l_l = LinkedList()
        l_l.add_tail(1)
        l_l.add_tail(2)
        l_l.add_tail(3)

        self.assertEqual(l_l.pop_tail(), 3)
        self.assertEqual(l_l.pop_tail(), 2)
        self.assertEqual(l_l.pop_tail(), 1)
        self.assertEqual(l_l.is_empty(), True)

    def test_print_linked_list(self):
        l_l = LinkedList()
        l_l.add_tail(1)
        l_l.add_tail(2)
        l_l.add_tail(3)
        f = io.StringIO()
        with redirect_stdout(f):
            print(l_l)
        self.assertEqual(f.getvalue(), "1,2,3\n")
