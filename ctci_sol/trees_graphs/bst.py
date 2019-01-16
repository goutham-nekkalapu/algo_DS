
'''
some definitions of a tree:
Height of node : 
 The height of a node is the number of edges on the longest downward path between that node and a leaf. A root node
 has highest height in a tree

Depth of a node:
 The depth of a node is the number of edges from the node to the tree's root node

Level of a node:
 The level of a node is defined by 1 + the number of connections between the node and the root.
 Level starts from '1'. i.e the level of root of a tree is '1'
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
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
                    temp.right = new_node
                    return
            else:
                if temp.left != None: # checking if the left child of temp is Null 
                    temp = temp.left
                else:
                    temp.left = new_node
                    return

    # deletes a node from bst tree 
    def delete(self, value):
        # locating the given value in BST 
        location = None      # location of 'value'
        prev = None          # parent of 'value'
        temp = self.root
        while temp:          # locating the node 
            if value == temp.value:
               location = temp
               break 
            elif value >temp.value:
                prev = temp
                temp = temp.right 
            else:
                prev = temp
                temp = temp.left
      
        if location == None: # given value is not in tree
           return -1
        elif location.left == None and location.right == None:
             new_node = None
        elif location.right == None:
             new_node = location.left
        else:                # assigning the left child of 'location' to its right child 
             temp = location.right 
             while temp.left:
                   temp = temp.left 
             temp.left = location.left
             new_node = location.right 

        # assigning new child to its parent 
        if prev == None: # this means the node requested to be deleted is 'root'
           self.root = new_node
        elif prev.left.value == value:
           prev.left = new_node
        else:
           prev.right = new_node

    # search for a value  in tree 
    def search(self, find_val):
        location = self.find_node(find_val) 
        if location == None:
           return False
        else:
            return True

    def print_tree(self):
        #return self.preorder_print(self.root, "")[:-1]
        #return self.inorder_print(self.root, "")[:-1]
        return self.postorder_print(self.root, "")[:-1]

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
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

    # returns the height of a tree, which is height of the root node 
    def heightof_tree(self):
        #return self.height(self.root)
        return self.get_height(self.root)
   
    # find the value in bst and returns its height 
    def node_height(self, value):
        location = self.find_node(value)
        #return self.height(location)
        return self.get_height(location)

    # calculates the height of a node
    def height(self, start):
        if start == None:
            return 0
        elif start.left == None and start.right == None:
            return 0
        else :
            left_h = self.height(start.left) + 1
            right_h = self.height(start.right) + 1
            if left_h > right_h :
                return left_h 
            else:
                return right_h

    # more elegant way of finding height 
    # this has lesser code than 'height()' implementation
    def get_height(self, start):
        if start == None:
           return -1
        return max(self.get_height(start.left), self.get_height(start.right)) + 1

    # returns depth of a node if in bst else '-1'
    def node_depth(self, value):
        depth = 0 
        found = 0 
        temp = self.root
        while temp and found == 0:
            if value == temp.value:
               found = 1 
            elif value > temp.value:
                temp = temp.right 
                depth += 1 
            else:
                temp = temp.left 
                depth += 1 
        # retrun depth if input value is in bst, else -1 
        if found:
            return depth
        else:
            return -1 

    # returns level of node 
    def node_level(self,value):
        # level is depth of a node + 1 
        return self.node_depth(value)+ 1 


if __name__ == "__main__":
   
    # creating a bst tree with root node = 4 
    tree = BST(4)
    
    #Insert elements 
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    tree.insert(9)

    #print 
    print ("the tree is : ")
    print(tree.print_tree())
    print(tree.heightof_tree())
   
    '''
    print(tree.heightof_tree())
    print(tree.node_depth(1))
    print(tree.node_depth(7))
    print(tree.node_depth(9))
    print(tree.node_level(9))
    '''
    
    '''
    # Check search
    # Should be True
    print (tree.search(4))
    
    # Should be True
    print (tree.search(6))

    tree.delete(1)
    print(tree.print_tree())
    '''
