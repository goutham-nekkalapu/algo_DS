
# delete the given node of a singly linkedlist given access to only this node. Also this node is neither at start ot et end.

import linkedlist as ll

# copy the values of next node to this node 
def delete_node_inbetween(node):
    node.data = node.next.data
    node.next = node.next.next
    pass

# getting the position of a node in linkedlist 
def get_node(node,position):
    count = 1
    while count != position and node:
          node = node.next
          count += 1
    return node

if __name__== "__main__":

  l1 = ll.LinkedList()

  l1.add(10)
  l1.add(20)
  l1.add(30)
  l1.add(40)
  l1.add(50)
  l1.add(60)
  l1.print()

  print("enter the position of the node you wish to delete ")
  position = int(input())

  node = get_node(l1.get_head(),position)
  delete_node_inbetween(node)
  print("modified linkedlist is")
  l1.print()
  


