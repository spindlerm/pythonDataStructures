""""Stack module"""
from typing import TypeVar
from linked_list import LinkedList

T = TypeVar("T")


class Stack:
    """ "Stack class implementation"""

    def __init__(self) -> None:
        """ "Initialise the stack"""
        self.items = LinkedList()

    def pop(self) -> T:
        """ "Pop an item from the stack"""
        if self.items.is_empty():
            raise ValueError("Stack is Empty")
        return self.items.pop_tail()

    def push(self, item: T) -> None:
        """ "Push an item to the stack"""
        self.items.add_tail(item)
