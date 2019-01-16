
# stack implementation 
# operations supported : push,pop,peek,isEmpty

class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
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
    print("hello")
    s1 = stack()
    print(s1.isEmpty())

    s1.push(10)
    s1.push(20)
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    s1.peek()

    """
    s1.push(10)
    s1.push(20)
    s1.push(10)
    s1.push(40)
    s1.push(50)
    s1.push(610)
    s1.push(90)
    s1.push(100)
    s1.print()
    s1.pop()
    s1.print()
    print(s1.peek())
    """
