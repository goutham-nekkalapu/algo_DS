
# check if linkedlist is a pallindrome or not 
# here I am assuming that elements of a linkedlist are integers 

import linkedlist as ll

# using stack and runner technique 
def is_LinkedlistPallindrome(l1):
    slow = l1.get_head()
    runner = slow
    stack = []
   
    # pushing first half of list to stack 
    while runner!= None and runner.next!=None :
          stack.append(slow.data)
          slow = slow.next 
          runner = runner.next.next

    print ("the first of linkedlist is :",stack)

    # skipping a position if list length is odd  
    if runner!= None:
       slow = slow.next

    # comparing the second half of list to check if is a pallindrome
    while slow:
        if slow.data != stack.pop():
           return False
        slow = slow.next 

    return True 

# to-do later 
# using recursion 
def is_Pallindrome_recursion(l1):
    head = l1.get_head()

    return 
        

if __name__ == "__main__":

  l1 = ll.LinkedList()

  l1.add(6)
  l1.add(5)
  l1.add(3)
  l1.add(5)
  l1.add(6)

  print("the input linkedlist is :")
  l1.print()

  print("is the given linkedlist a pallindrome ?")
  print("Ans :",is_LinkedlistPallindrome(l1))

