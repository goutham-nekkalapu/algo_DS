
# a. we have to perform the sum of two numbers which are given in two seperate lists. the result should also be in a linkedlist
#    Eg : adding 345 and 619 ; Note : The inputs need not be of same length 
#         input format : 
#                       5->4->3
#                       9->1->6
#               output  4->6->9 
#
# b. Everything is same as above except that inputs are given in normal order as we read 
#    Eg : 
#        input format :
#                      3->4->5
#                      6->1->9
#              output  9->6->4

import linkedlist as ll

# solution for porblem 'a' 
def add_1(l1,l2):
    n1 = l1.get_head()
    n2 = l2.get_head()
     
    # to manage new list where sum is stored 
    head = ll.Node(-1)
    tail = head
    val = 0 
    
    # while stops if both lists reach to the end  
    while n1!=None or n2!=None:
          if n1 == None:
             val = val + n2.data 
             n2 = n2.next
          elif n2 == None:
             val = val + n1.data 
             n1 = n1.next
          else:
             val = val + n1.data + n2.data
             n1 = n1.next
             n2 = n2.next

          temp = ll.Node(val %10)
          tail.next = temp
          tail = temp
          val = int(val/10)

    return head.next

# solution for problem 'b' using stack   
# time comlexity O(n); space complexity O(m) m = length of the longest linkedlist 
def add_2_stack(l1,l2):
    n1 = l1.get_head()
    n2 = l2.get_head()
     
    # to store the input lists
    stack1 = []
    stack2 = []

    # for calculating the lengths of input linkedlist
    length1 = 0
    length2 = 0

    # pushing the digits of each list onto the stack
    while n1!=None or n2!=None:
          if n1 == None:
             stack2.append(n2.data) 
             n2 = n2.next
             length2 += 1
          elif n2 == None:
             stack1.append(n1.data) 
             n1 = n1.next
             length1 += 1
          else:
             stack1.append(n1.data) 
             stack2.append(n2.data) 
             length1 += 1
             length2 += 1
             n1 = n1.next
             n2 = n2.next
   
    # finding the shortest list
    if length1 > length2 :
        length = length1
    else:
        length = length2
    
    # to manage new list where sum is stored 
    head = ll.Node(-1)
    val = 0 

    # poping from stack, performing addition, creating new list
    while length:
          x = 0
          y = 0
          if stack1:
             x = stack1.pop() 
          if stack2:
             y = stack2.pop()
           
          val = val + x + y  
          temp = ll.Node(val %10)
          val = int(val/10)
          temp.next = head.next
          head.next = temp
          length -= 1

    return head.next

# solution for porblem 'b' using recursion
def add_2_recursion(l1,l2):
    n1 = l1.get_head()
    n2 = l2.get_head()
    
    len1 = get_listlength(n1) 
    len2 = get_listlength(n2) 
   
    if len1 < len2:
       n1 = padzerosto_list(n1, len2-len1) 
    else:
       n2 = padzerosto_list(n2, len1-len2) 

    head = ll.Node(-1)
    add_recursion(n1,n2,head)
    return head.next

# helper function to add_2_recursion which is called recursively
def add_recursion(n1,n2,head):
    if n1 == None and n2 == None:
       return 0
    else:
       val = n1.data + n2.data + add_recursion(n1.next,n2.next,head)

    temp = ll.Node(val %10)
    val = int(val/10)
    temp.next = head.next
    head.next = temp
    return val 

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

# returns the length of linkedlist 
def get_listlength(node):
    length = 0
    while node:
          length += 1 
          node = node.next 
    return length

# pads zeros at the start of the linkedlist 
def padzerosto_list(head,num):
    while num:
          node = ll.Node(0)
          node.next = head
          head = node
          num -= 1
    return head


# main function 
if __name__ == "__main__":

  l1 = ll.LinkedList()
  l2 = ll.LinkedList()

  """
  # test cases to test prob 'a'
  l1.add(3)
  l1.add(4)
  l1.add(5)

  l2.add(6)
  l2.add(1)
  """
  # test cases for prob 'b'   
  l1.add(5)
  l1.add(4)
  l1.add(3)

  l2.add(1)
  l2.add(2)
  
  print("the input linkedlists are :")
  l1.print()
  l2.print()
 
  """
  node = add_1(l1,l2)
  print("the sum of inputs is :")
  print_list(node)

  node = add_2_stack(l1,l2)
  print("the sum of inputs is :")
  print_list(node)
  """
  node = add_2_recursion(l1,l2)
  print("the sum of inputs is :")
  print_list(node)

