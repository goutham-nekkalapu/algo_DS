
"""
Implement a func if a tree is balanced or not. 
A tree is balanced if the heights of subtrees of every node of the tree differ by atmost '1'

"""
from bst import * 

# using default get_height() function of tree.
# input arguments : 'tree' object and 'root' node
# here we are calling get_height for every node of the tree
# and it traverses the subtrees for every call, which is a bit redundant 
def is_balanced(tree, node):
    
    if node == None:
       return True 
    
    height_diff = tree.get_height(node.left) - tree.get_height(node.right)
    if abs(height_diff) > 1:
       return False
    else:
       return is_balanced(tree, node.left) and is_balanced(tree, node.right)

# using modified get_height() function 
# time complexity : O(n) has to traverse 'n' elements
# space complexity : O(n); n recusive calls so requires stack space of 'n'
def check_height(node):
    err_msg = "not_balanced"
    if node == None:
        return -1

    left_h = check_height(node.left)
    if left_h == err_msg:
        return err_msg  # pass error up 
        
    right_h = check_height(node.right)
    if right_h == err_msg:
        return err_msg # pass error up 

    height_diff = left_h - right_h
    if abs(height_diff) > 1:
        return err_msg # found that sub-tree is not balanced
    else:
        return max(left_h, right_h)+ 1 

def is_balanced_2(root):
    err_msg = "not_balanced"
    return check_height(root) != err_msg

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

    # expected : False 
    print("is the input tree balanced ? : ",is_balanced(tree, tree.root))

    t1 = BST(4)
    #Insert elements 
    t1.insert(2)
    t1.insert(5)
    
    # expected : True
    print("is the input tree balanced ? : ",is_balanced(t1, t1.root))


    # expected : False 
    # using is_balanced_2 func, which inturn uses a modified fun height_fun
    print("is the input tree balanced ? : ",is_balanced_2(tree.root))
