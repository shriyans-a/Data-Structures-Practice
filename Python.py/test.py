class Node:
    def  __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.length += 1
    
    def print_list(self):
        while self.head is not None:
            print(self.head.value)
            self.head = self.head.next

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1


    def pop_first(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None


        
    
    

mylinkedlist = LinkedList(1)
mylinkedlist.append(2)
mylinkedlist.prepend(0)
mylinkedlist.print_list()
mylinkedlist.pop_first()
mylinkedlist.print_list()