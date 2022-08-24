
def name_to_number(name):
    match name:
        case 'камень':
            return 0
        case 'спок':
            return 1
        case 'бумага':
            return 2
        case 'ящерица':
            return 3
        case 'ножницы':
            return 4
        case _:
            return -1


def number_to_name(number):
    match number:
        case 0:
            return 'камень'
        case 1:
            return 'спок'
        case 2:
            return 'бумага'
        case 3:
            return 'ящерица'
        case 4:
            return 'ножницы'
        case _:
            return -1


# Узел списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Двусвязный циклический список
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = Node(data)
            self.head.next = self.head
            self.head.prev = self.tail
        else:
            new_node = Node(data)

            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.tail = new_node
            new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next

            if cur.next == self.head:
                print(self.tail.data)
                break


cddl = CircularDoublyLinkedList()
