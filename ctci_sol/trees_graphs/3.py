
"""
4.3 :
given a binary tree, create linkedlists of all nodes at each depth i.e if you have a tree of depth 'D', we will have 'D' linked lists 
"""

from bst import *

# global variables to store node values at each depth of the tree
lists =[[]]
list_len = len(lists)

def get_depth_lists(root):
    return preorder_trav_modif(root, "", 0)[:-1]

# modified pre-order traversal to store values of node at each depth 
# time complexity O(n) for traversing through 'n' elements 
# space complexity O(log N) + O(N) ; since the func is called recursively O(log N) times, 
# it occupies same amount of space on stack memory. the O(N) is for storing the elements in lists 
def preorder_trav_modif(start, traversal, depth):
    global list_len
    global lists
    if start:
       traversal += (str(start.value) + "-")
       if list_len - 1 < depth:
           lists.append([])
           list_len += 1
       lists[depth].append(start.value) 
       traversal = preorder_trav_modif(start.left, traversal, depth+1)
       traversal = preorder_trav_modif(start.right, traversal, depth+1)
    return traversal


# bfs using iteration on a directed graph
def bfs_directed(graph, start):
    visited = []
    queue= [start]

    while queue:
        vertex = queue.pop(0)
        if vertex[0] not in visited and vertex[1] == 1:
            visited.append(vertex[0])
            for node in graph[vertex[0]]:
                if node[0] not in visited:
                    queue.append(node)
    return visited

# modified bfs to store values of node at each depth 
# time complexity O(N) to traverse the 'N' nodes 
# space complexity O(N) to store the lists 
def bfs_directed_modif(graph, start, depth=0):
    global list_len
    global lists
    
    visited = []
    start = start + (depth,)
    queue= [start]

    while queue:
        vertex = queue.pop(0)
        if vertex[0] not in visited and vertex[1] == 1:
            visited.append(vertex[0])
            # increasing the depth for every new level of tree
            if depth != vertex[2]:
               depth += 1
            
            if list_len - 1 < depth:
               lists.append([])
               list_len += 1

            # iserting in the lists 
            lists[depth].append(vertex[0])
            
            # queuing every node in each level
            for node in graph[vertex[0]]:
                if node[0] not in visited:
                    node = node + (depth+1,)
                    queue.append(node)
    return visited


if __name__ == "__main__":

    """
    tree = BST(4)

    #Insert elements 
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    tree.insert(9)
 
    print ("the list of node values at each depth are : ")
    get_depth_lists(tree.root)
    print(lists)
    """

    # a tree can be treated as a directed graph. 
    # Forming directed graph from the above tree 
    graph_directed =  {
                '4': [('2',1), ('5',1)],
                '2': [('1',1), ('3',1), ('4',0)],
                '5': [('7',1), ('4',0)],
                '1': [('2',0)],
                '3': [('2',0)],
                '7': [('9',1), ('5',0)],
                '9': [('7',0)],
            }

    """
    # ['4', '2', '5', '1', '3', '7', '9']
    bfs_out = bfs_directed(graph_directed,('4',1)) # find BFS on given graph starting from 'C'
    print(bfs_out)
    """
    
    bfs_out = bfs_directed_modif(graph_directed,('4',1),0) # find BFS on given graph starting from 'C'
    print ("using BFS to calculate the ")
    print ("the list of node values at each depth are : ")
    print(lists)
