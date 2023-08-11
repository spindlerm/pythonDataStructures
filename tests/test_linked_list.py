import unittest
from linked_list import LinkedList


class TestStack(unittest.TestCase):
  def test_is_empty_when_empty(self):
        l = LinkedList()
        self.assertEquals(True, l.is_empty())

  def test_is_empty_when_not_empty(self):
      l = LinkedList()
      l.add_tail(1)
      self.assertEquals(False, l.is_empty())

  def test_get_head_when_empty(self):
        l = LinkedList()
        self.assertRaises(ValueError, l.get_head)

  def test_tail_head_when_empty(self):
      l = LinkedList()
      self.assertRaises(ValueError, l.get_tail)

  def test_add_one_item(self):
      l = LinkedList()
      l.add_tail(1)
      self.assertEquals(l.get_tail(),1)

  def test_add_multiple_items(self):
      l = LinkedList()
      l.add_tail(1)
      l.add_tail(2)
      l.add_tail(3)
      self.assertEquals(l.get_head(),1)
      self.assertEquals(l.get_tail(),3)

  def test_pop_head(self):
      l = LinkedList()
      l.add_tail(1)
      l.add_tail(2)
      l.add_tail(3)
      self.assertEquals(l.pop_head(),1)
      self.assertEquals(l.pop_head(),2)
      self.assertEquals(l.pop_head(),3)
      self.assertEquals(l.is_empty(), True)

  def test_pop_tail(self):
      l = LinkedList()
      l.add_tail(1)
      l.add_tail(2)
      l.add_tail(3)
      self.assertEquals(l.pop_tail(),3)
      self.assertEquals(l.pop_tail(),2)
      self.assertEquals(l.pop_tail(),1)
      self.assertEquals(l.is_empty(), True)