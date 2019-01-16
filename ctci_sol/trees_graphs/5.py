
'''
check if a binary tree is a binary search tree or not 
'''

from bst import * 

# checks if given list is in ascending order or not 
def is_ascending(input_list):
    prev = input_list[0]
    for num in input_list:
        if num < prev:
           return False
        prev = num 
    return True  

# checks if a given tree is a Binary search tree or not
# does in-order traversal first and check if it is in ascending order  
def is_bst(tree):
    tree.root
    inorder_trav = tree.inorder_print(tree.root, "")[:-1]
    # remove '-'
    inorder_trav = inorder_trav.split('-')
    input_list = []
    for i in inorder_trav:
        input_list.append(int(i))
    return is_ascending(input_list) 

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

    print("is the given tree a BST ? ",is_bst(tree))    


