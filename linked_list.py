""""LinkedList module"""
from dataclasses import dataclass, field
from typing import TypeVar

T = TypeVar("T")


@dataclass
class Node:
    """ "Node data class"""

    value: T
    prev: "Node" = field(default=None)
    next: "Node" = field(default=None)


class LinkedList:
    """ "LinkedList class"""

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """ "Checks if the list is empty"""
        return self.head is None

    def get_head(self) -> Node:
        """ "Returns the head of the list"""
        if self.head is None:
            raise ValueError("Linked list is empty")
        return self.head.value

    def pop_head(self) -> Node:
        """ "Returns and removes the head of the list"""
        if self.head is None:
            raise ValueError("Linked list is empty")
        node = self.head
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next
        return node.value

    def get_tail(self) -> Node:
        """ "Returns the tail of the list"""
        if self.tail is None:
            raise ValueError("Linked list is empty")
        return self.tail.value

    def pop_tail(self) -> Node:
        """ "Returns and removes the tail of the list"""
        if self.tail is None:
            raise ValueError("Linked list is empty")
        node = self.tail
        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        return node.value

    def add_tail(self, value: T) -> None:
        """ "Add item to the tail/end of the list"""
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def __str__(self) -> str:
        r_v = ""
        len(r_v)
        pos = self.head
        while pos is not None:
            r_v = r_v + (str(pos.value) if len(r_v) == 0 else "," + str(pos.value))
            pos = pos.next

        return r_v
