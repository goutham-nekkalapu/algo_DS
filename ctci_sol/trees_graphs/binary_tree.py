
import random 

class node():
    def __init__(self,num):
        self.value = num 
        self.left = None
        self.right = None

def create_binary_tree(depth):
    if depth > 0:
        x = random.randint(1,101)
        n1 = node(x)
        n1.left = create_binary_tree(depth-1)
        n1.right = create_binary_tree(depth-1)
        return n1
    else:
        return None

def print_tree(root):
    return in_order(root, "")[:-1]

def in_order(n,traversal):
    if n:
       traversal += (str(n.value) + '-')
       traversal = in_order(n.left, traversal)
       traversal = in_order(n.right, traversal) 
    return traversal

if __name__ == "__main__":
    print ("enter the depth of the binary tree desired ")
    depth = int(input())
    root  = create_binary_tree(depth)
    print (print_tree(root))

