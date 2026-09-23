from Node import Node

class LinkedList:
    """
    Empty Constructor
    
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_begging_with_tail(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    
    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def display(self):
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
