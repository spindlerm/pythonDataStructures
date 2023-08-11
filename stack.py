from linked_list import LinkedList


class Stack:
    def __init__(self) -> None:
        self.items = LinkedList()

    def pop(self) -> int:
        if self.items.is_empty():
            raise ValueError("Stack is Empty")
        else:
            return self.items.pop_tail().value

    def push(self, item: int) -> None:
        self.items.add_tail(item)
