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
            pass

        def insert(self, index, value):
            pass