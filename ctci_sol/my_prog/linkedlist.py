
# node structure of a linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list 
class LinkedList:
    def __init__(self):
        self.head = None

    # adding an element at start of linkedlist
    def add(self,d):
        node = Node(d)
        if self.head == None:
           self.head = node
        else:
           node.next = self.head
           self.head = node 
        return True 

    def search(self, d):
        node = self.head 
        while node:
            if node.data == d:
                return True
            else:
                node = node.next
        return False

    def print(self):
        node = self.head
        while node:
            print(node.data,end =" ")
            if node.next!= None:
               print("-->", end =" ")
            node = node.next
        print()

    def remove(self,d):
        if self.head.data == d:
           self.head = self.head.next
           return True
        else:
           node = self.head.next
           prev = self.head
           while node:
            if node.data == d:
               prev.next = node.next
               return True
            else:
                prev = node
                node = node.next
        return False

if __name__ == "__main__":
    print(" a single linked list ")
    l1 = LinkedList() 
    l1.add(10)
    l1.add(20)
    l1.add(30)
    l1.print()
    l1.remove(20)
    l1.add(40)
    l1.add(50)
    l1.print()
    print(l1.search(50))
    print(l1.search(90))

