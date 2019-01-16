
"""
this bst is same as a normal binary search tree, except each node can reach its parent node as well.
the root node's parent will be 'None' 

"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
   
class BST_modified(object):
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, new_val):
        new_node = Node(new_val)
        temp = self.root

        while temp:
            if new_val > temp.value:
                if temp.right != None: # checking if the right child of temp is Null
                    temp = temp.right
                else:
                    new_node.parent = temp.right 
                    temp.right = new_node
                    return
            else:
                if temp.left != None: # checking if the left child of temp is Null 
                    temp = temp.left
                else:
                    new_node.parent = temp.left
                    temp.left = new_node
                    return

    def print_tree(self):
        #return self.preorder_print(self.root, "")[:-1]
        return self.inorder_print(self.root, "")[:-1]
        #return self.postorder_print(self.root, "")[:-1]

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    # returns the node if it has the requested value
    def find_node(self, find_val):
        # starts searching from the root
        temp = self.root
        while temp:
            if find_val == temp.value:
                return temp
            elif find_val > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return None

    # takes a 'value' of a node as an input and returns the node's
    # inorder successor
    def find_inorder_successor(self, value):
        node = self.find_node(value)
        return self.inorder_successor(node)

    # finds the inorder successor and returns its location
    # for a given the location of input node.
    # If there is no inorder successor, returns 'None' 
    def inorder_successor(self, node):

        # if node is None
        if node == None:
           return None
 
        if node.right != None:
           return self.leftmost_child(node.right) 
        else:
           parent = node.parent
           while parent != None and parent.left != node:
                 node = parent 
                 parent = node.parent
        return parent 
      
    # returns the location of left most node for a given node
    def leftmost_child(self, node):
        if node == None:
           return None
       
        while node.left != None:
              node = node.left
        return node
 
