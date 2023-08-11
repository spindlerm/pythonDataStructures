from typing import TypeVar
from linked_list import LinkedList

T= TypeVar('T')

class Stack:
    def __init__(self) -> None:
        self.items = LinkedList()

    def pop(self) -> T:
        if self.items.is_empty():
            raise ValueError("Stack is Empty")
        else:
            return self.items.pop_tail()

    def push(self, item: T) -> None:
        self.items.add_tail(item)
