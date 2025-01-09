class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append_list(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_list(self):
        
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend_list(self, value):
        
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
            

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return False
        
        if self.length == 0:
            self.prepend(value)
        
        if self.length == index:
            self.append_list(value)
        
        temp = self.head
        pre = temp
        for _ in range(index):
            pre = temp
            temp = temp.next
        pre.next = new_node
        new_node.next = temp
        return True
    
    def remove(self, index):

        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        temp = self.get(index+1)
        pre = self.get(index-1)
        pre.next.next = None
        pre.next = temp
        self.length -= 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



