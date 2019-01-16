
# queue data structure implementation 
# operations supported are add, remove, peek, isEmpty  


class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self,item):
        self.items.insert(0,item)

    def remove(self):
        if self.isEmpty():
            print ("stack is empty : pop can not be done")
        else:
            return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print ("stack is empty : peek can not be done")
        else:
            return self.items[-1]

    def print(self):
        if self.isEmpty():
            print ("stack is empty")
        else:
            print(self.items)

if __name__ == "__main__":
   q1 = queue()
   q1.add(10)
   q1.add(20)
   q1.add(30)
   q1.add(40)
   q1.print()
   print(q1.isEmpty())
   q1.remove()
   q1.print()
   print(q1.peek())
   q1.print()







