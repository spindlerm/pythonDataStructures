from dataclasses import dataclass, field


@dataclass
class Node:
    value: int
    prev: 'Node' = field(default=None)
    next: 'Node' = field(default=None)


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        return self.head is None

    def get_head(self) -> Node:
        if self.head is None:
            raise ValueError("Linked list is empty")
        return self.head.value

    def pop_head(self) -> Node:
        if self.head is None:
            raise ValueError("Linked list is empty")
        v = self.head.value
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next
        return v

    def get_tail(self) -> Node:
        if self.tail is None:
            raise ValueError("Linked list is empty")
        return self.tail.value

    def pop_tail(self) -> Node:
        if self.tail is None:
            raise ValueError("Linked list is empty")
        v = self.tail.value
        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        return v

    def add_tail(self, value) -> None:
        n = Node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
