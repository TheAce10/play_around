class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)