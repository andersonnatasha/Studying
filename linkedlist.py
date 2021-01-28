class Node():
    """A node."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    """A linked list."""cd 

    def __init__(self):
        self.head = None
        self.tail = None


def create_most_basic_linked_list():
    """Create a linked list with no values
    >>> print(create_most_basic_linked_list())
    None

    """
    my_ll = LinkedList()

    return my_ll.head



if __name__ == '__main__':
    import doctest
    print()
    result = doctest.testmod()
    if not result.failed:
        print('ALL TESTS PASSED!')
    print()
