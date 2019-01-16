
# partition a linked list based based on the input 'x' given. (note that this is not sorting the linkedlist) 

import linkedlist as ll

# time complexity is O(n)
# the sequence of numbers of each section is not disturbed with this func call
def partition(input_list,x):

    # pointers to add at the end of two lists 
    n1 = ll.Node(-1)
    n2 = ll.Node(-1)
   
    # head pointers of both the lists 
    l1_head = n1
    l2_head = n2 

    node = input_list.get_head()
    while node:
          if node.data < x:
             n1.next = node
             n1 = node 
          else:
             n2.next = node
             n2 = node
          node = node.next

    n2.next = None
    n1.next = l2_head.next
    return l1_head.next

# by using this function, in the generated list, sequence < x will be in reverse order from original appearance
def partition_reverse(input_list,x):

    # head is start node of list which is < x 
    # tail is start node of list which is > x
    head = input_list.get_head()  
    tail = input_list.get_head()  

    # all of them are covered at the end 
    node = input_list.get_head()  
    while node:
        next_node = node.next
        if node.data < x:
           node.next = head
           head = node
        else:
            tail.next = node
            tail = node
        node = next_node

    tail.next =node
    return head
     

# print the list from a given node 
def print_list(node):
    if node == None:
       print(" Linked list is empty")
       return None
    while node:
         print(node.data,end =" ")
         if node.next!= None:
            print("-->", end =" ")
         node = node.next
    print()
    pass 


if __name__ == "__main__":
 
  l1 = ll.LinkedList()
  l1.add(10)
  l1.add(20)
  l1.add(80)
  l1.add(25)
  l1.add(30)
  l1.add(40)
  l1.add(45)
  l1.add(35)
  l1.add(50)
  l1.add(60)
  l1.print()

  print("enter a number according by which list has to be partitioned")
  x = int(input()) 
 
  """
  new_head = partition(l1,x)
  print("the partitioned list is :")
  print_list(new_head)
  """

  new_head = partition_reverse(l1,x)
  print("the partitioned list is :")
  print_list(new_head)

