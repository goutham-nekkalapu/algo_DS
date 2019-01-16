
"""
inserting a sorted array of unique elements to a BST in such a way that BST has minimal height   
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def create_bst_min_height(input_list):
    return bst_min_height(input_list, 0, len(input_list)-1)

# creates a bst tree for a given sorted list with minimum height 
# Time complexity : the time complexity of forming this bst would be : O(n) as 
# here we are using recursive fun to append each sub-array to a node 
def bst_min_height(input_list, start, end):
    if end < start:
       return None
    
    mid = (start + end)//2
    new_node = Node(input_list[mid]) 
    new_node.left = bst_min_height(input_list, start, mid-1) 
    new_node.right = bst_min_height(input_list, mid+1, end) 
    return new_node

def print_tree(root):
    return preorder_print(root, "")[:-1]
    #return inorder_print(root, "")[:-1]
    return self.postorder_print(tree.root, "")[:-1]

def preorder_print(start, traversal):
    if start:
       traversal += (str(start.value) + "-")
       traversal = preorder_print(start.left, traversal)
       traversal = preorder_print(start.right, traversal)
    return traversal

# calculates the height of a node; if node == root returns height of tree 
def height(start):
    if start == None:
       return 0
    elif start.left == None and start.right == None:
         return 0
    else :
         left_h = height(start.left) + 1
         right_h = height(start.right) + 1
         if left_h > right_h :
              return left_h
         else:
              return right_h

if __name__ == "__main__":
   l1 = [1,2,3,4,5,6,7,8,9] 

   tree_root = create_bst_min_height(l1) 
   
   # pre-order traversal result : 5-2-1-3-4-7-6-8-9 
   print (print_tree(tree_root))
   print (height(tree_root))
