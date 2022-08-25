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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return self.data


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        n = 1

        cur = self.head

        while cur.next is not self.head:
            n += 1
            cur = cur.next

        return n

    def __str__(self):
        cur = self.head
        lst = ''

        while cur:
            lst += str(cur.data)
            lst += ', '
            cur = cur.next

            if cur.next == self.head:
                lst += str(self.tail.data)
                break

        return lst

    def __getitem__(self, item):
        i = 0
        cur = self.head

        if item < len(self):
            while item is not i:
                cur = cur.next
                i += 1
        else:
            raise IndexError

        return cur

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


cdll = CircularDoublyLinkedList()

cdll.append('1')
cdll.append('2')
cdll.append('3')
cdll.append('4')
cdll.append('5')

print(cdll[4])
print(len(cdll))
print(cdll)
pass
