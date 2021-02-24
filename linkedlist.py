class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f'<LL: {self.head}>'

    def insert(self, data):
        """Insert data into a linked list
        >>> ll = LinkedList()
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> ll.head.data
        1
        >>> ll.tail.data
        2
        """

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = new_node

        self.tail = new_node

    def view(self):
        """print each item in a linked list
        >>> ll = LinkedList()
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> ll.insert(3)
        >>> ll.insert(4)
        >>> ll.view()
        [1, 2, 3, 4]
        """

        view = []
        current = self.head
        while current:
            view.append(current.data)
            current = current.next

        print(view)

    def search(self, data):
        """find and item in a linked list
        >>> ll = LinkedList()
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> ll.insert(3)
        >>> ll.insert(4)
        >>> ll.search(3)
        True
        """

        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def delete(self, target):
        """remove data from a linked list
        >>> ll = LinkedList()
        >>> ll.insert(0)
        >>> ll.insert(1)
        >>> ll.insert(2)
        >>> ll.insert(3)
        >>> ll.delete(2)
        >>> ll.view()
        [0, 1, 3]
        """

        if not self.head:
            return

        if self.head.data == target:
            self.head = self.head.next
            return self.head

        current = self.head
        while current and current.next:
            if current.next.data == target:
                current.next = current.next.next
                if current.next == None:
                    self.tail = current
                return
            current = current.next


if __name__ == '__main__':
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print('ALL TESTS PASSED')
    print()
