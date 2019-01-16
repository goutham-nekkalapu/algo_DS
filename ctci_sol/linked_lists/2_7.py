
# check if two linkedlists intersect or not. If they intersect, return the node at which they intersect 
# other approaches:
# 1. can use hash table 
# 2. can traverse the lists and redirect them to each other, see below 

import linkedlist as ll
import random

#### approach -2:
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = headA
        l2 = headB 
        count = 0 
        
        while l1 and l2:
          if l1 == l2:
            return l1
          
          l1 = l1.next
          l2 = l2.next
          
          if l1 == None and l2:
            l1 = headB
            count += 1

          if l2 == None and l1:
            l2 = headA
            count += 1
            
          if count > 2:
            return None
          
        return None 

# returns True if given lists intersect, else False
def check_ifIntersect(head1, head2):
    n1 = head1
    n2 = head2

    while n1.next!= None:
        n1 = n1.next

    while n2.next!= None:
        n2 = n2.next

    if n1 == n2:
        return True
    else:
        return False  

# returns the intersecting node of both lists else returns 'None'
def find_commonNode(head1,head2):
   
    # if linkedlists are not intersecting return None
    if not check_ifIntersect(head1, head2):
        return None
    
    # calcualting the lengths of both the lists 
    n1 = head1
    l1 = 0 
    while n1:
        l1 += 1
        n1 = n1.next
    
    n2 = head2
    l2 = 0 
    while n2:
        l2 += 1
        n2 = n2.next

    # padding zeros at the start of linkedlist 
    if l1 < l2:
       head1 = padzerosto_list(head1,l2-l1)
    else:
       head2 = padzerosto_list(head2,l1-l2)

    # while traversing the lists checking if any of nodes of lists are same  
    while head1:
          if head1 == head2:
             return head1
          else:
             head1 = head1.next
             head2 = head2.next
             
# pads zeros at the start of the linkedlist 
def padzerosto_list(head,num):
    while num:
          node = ll.Node(0)
          node.next = head
          head = node
          num -= 1
    return head

# create linkedlists to test 
def create_testcases(val):
    
    # creating fist section of l1 
    x = random.randint(1,7)
    count = 0 
    while count < x:
          temp = ll.Node(random.randint(20,30))
          if count == 0:
             head1 = temp
          else:
             tail1.next = temp
          tail1 = temp 
          count += 1
   
    # creating fisrt section of l2 
    x = random.randint(1,8)
    count = 0 
    while count < x:
          temp = ll.Node(random.randint(30,40))
          if count == 0:
             head2 = temp
          else:
             tail2.next = temp
          tail2 = temp 
          count += 1
   
    # creating second section of lists   
    head3 = None
    x = random.randint(1,6)
    print ("the value of x is :",x)
    count = 0 
    while count < x:
          temp = ll.Node(random.randint(1,20))
          temp.next = head3 
          head3 = temp
          count += 1
    
    head4 = None
    x = random.randint(1,7)
    count = 0 
    while count < x:
          temp = ll.Node(random.randint(1,20))
          temp.next = head4
          head4 = temp
          count += 1

    # for val == 1 create positive testcase and for '0' create negative testcase
    if val == 1:
       tail1.next = head3
       tail2.next = head3
    else:
       tail1.next = head3
       tail2.next = head4

    print("list that is common to both : ")
    print_list(head3)
    return (head1,head2)

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
 
   print ("enter 1 to generate positive test cases else 0")
   val = int(input()) 
   head1, head2 = create_testcases(val)
   print_list(head1)    
   print_list(head2)    
   print("are given linkedlists intersecting ? ")
   thereis_intersect = check_ifIntersect(head1,head2)
   print("ans : ", thereis_intersect )
  
   if thereis_intersect:
      node = find_commonNode(head1,head2)
      print ("the lists intersect at node : ",node)
      print ("data present at intersection is : ",node.data)
 
