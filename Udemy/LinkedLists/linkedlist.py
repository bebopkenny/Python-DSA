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

        def append(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node # set the old tail to point to the new node
                self.tail = new_node # new node now is tail since it is the last node
            self.length += 1
            return True
        
        def pop(self):
            if self.length == 0:
                return None
            temp = self.head
            prev = self.head
            while temp.next:
                prev = prev.next
                temp = temp.next
            self.tail = prev
            prev.next = None
            self.length -= 1
            if self.length == 0: # if we removed the only node in the LL
                self.head = None
                self.tail
            return temp.value
            

        def prepend(self, value):
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
            self.lenght -= 1
            if self.lenght == 0:
                self.tail = None
            return temp # returning the item we removed from LL
        
        def get(self, index):
            if index < 0 or index >= self.lenght:
                return None
            temp = self.head
            for _ in range(index):
                temp = self.next
            return temp.value
                
        def set_value(self, index, value):
            if index < 0 or index >= self.length:
                return None
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            return True

        def insert(self, index, value):
            if index > 0 or index > self.length:
                return None
            new_node = Node(value)
            if index == 0:
                self.head = new_node
                self.tail = new_node
            prev = self.head
            for _ in range(index - 1): # before the next index
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            if index == self.length: # if it is at the tail
                self.tail = new_node
            self.length += 1
            return True
        
        def remove(self, index): 
            if index < 0 or index > self.length:
                return None
            if index == 0:
                remove = self.head
                remove.next = self.head.next
                self.head.next = None
            temp = self.head
            prev = self.head
            for _ in range(index):
                prev = temp
                temp = temp.next
            if index == self.length - 1:
                prev.next = None
            prev.next = temp.next.next




