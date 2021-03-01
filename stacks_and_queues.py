class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node {self.data}>'


class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f'<Head {self.head.data}, Tail {self.tail.data}>'

    def is_empty(self):
        return self.head

    def peek(self):
        return self.head.data

    def add(self, data):

        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

        if not self.head:
            self.head = new_node

    def remove(self):

        if not self.head:
            return
        data = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return data


class Stack:

    def __init__(self):
        self.top = None

    def __repr__(self):
        return f'<Top {self.top.data}>'

    def is_empty(self):
        return not bool(self.top)

    def peek(self):
        if not self.top:
            return

        return self.top.data

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top

        self.top = new_node

    def pop(self):

        if not self.top:
            return

        data = self.top.data
        self.top = self.top.next
        return data
