
# find if a linnkedlist has a cycle. If so return the start node of cycle

import linkedlist as ll 
import random 

# returns 'True' of there is a cycle in linkedlist else returns 'False'
def isthere_cycle(head):

    # pointers to traverse the linkedlist
    slow   = head
    runner = head  

    # iterating through the linkedlist with two pointers. 'Runner' is one position
    # ahead of 'slow' i.e it jumps one node every time. If there is a loop they would
    # meet at some time. If no loops runner hits end of list, None value first 
    while runner!=None and runner.next!=None:
          runner = runner.next.next
          slow = slow.next
          if runner == slow:
             return True 

    # checking if runner has reached end of list, if yes no loop in linkedlist
    if runner == None or runner.next == None:
        return False

def cycle_start(head):

    result  = isthere_cycle(head)
    if result == False:
        return None

    slow   = head 
    runner = head 
  
    # already checked that there is a cycle
    # both pointers 'runner' and 'slow' collide and they are 'k' distance away from start of cycle
    # which is the same distance 'head' start of linkedlist is away from cycle start 
    while runner!=None and runner.next!=None:
          runner = runner.next.next
          slow = slow.next
          if runner == slow:
             break

    # traversing the linkedlist using 'slow' from start of list and from where both 'slow' and 'runner'
    # first collided. Again slow and first will collide after k nodes.
    slow = head 
    while slow != runner:
          slow = slow.next 
          runner = runner.next
    return runner 

# function to create test cases 
def create_testcases(val):

    # creating fist section of list
    x = random.randint(1,8)
    count = 0
    while count < x:
          temp = ll.Node(random.randint(1,20))
          if count == 0:
             head1 = temp
          else:
             tail1.next = temp
          tail1 = temp
          count += 1

    # creating second section of list 
    x = random.randint(1,10)
    count = 0
    while count < x:
          temp = ll.Node(random.randint(25,40))
          if count == 0:
             head2 = temp
          else:
             tail2.next = temp
          tail2 = temp
          count += 1
    
    # if val == '1', we create a linkedlist with a cycle else without cycle 
    if val == 1:
       tail1.next = head2 
       tail2.next = tail1
    else:
       tail1.next = head2
    return (head1,tail1)


# print the list from a given node 
def print_listwithcycle(node,loop_start,val):
    if node == None:
       print(" Linked list is empty")
       return None
    if val != 1:
       while node:
             print(node.data,end =" ")
             if node.next!= None:
                print("-->", end =" ")
             node = node.next
    else:
       # if there is a loop in linkedlist  
       count = 0 
       while count < 2:
             print(node.data,end =" ")
             node = node.next
             if node == loop_start:
                count += 1
             if count < 2:
                print("-->", end =" ")

    print()
    pass


if __name__ == "__main__":
   print ("enter 1 to create linkedlist with a cycle")
   val = int(input())
   (head,loop_start) = create_testcases(val)
   
   print("the input linkedlist is :")
   print_listwithcycle(head,loop_start,val)

   print ("the loop starts at node : ",loop_start)
   print ("data at start of loop is : ",loop_start.data)

   print ("does the linkedlist has a loop ? ")
   print ("ans : ",isthere_cycle(head))
  
   result = cycle_start(head)
   if result == None :
       print ("there is no cycle")
   else:
       print ("the cycle in linkedlist starts at :")
       print ("node -- ",result)
       print ("value at cycle start : ",result.data)

