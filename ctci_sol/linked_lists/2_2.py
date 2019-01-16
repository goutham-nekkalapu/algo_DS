
# finding the kth to last element of a singly linked list 

import linkedlist as ll

# using runner technique. The runner first traversers the first 'k' positions of the list. 
# Then currrent will start from head along with runner, till runner reaches end, at which point current is at position 'k' from end 
def find_kthto_last(head,position):
    current = head 
    runner = head
    count = 0
   
    while runner and count != position:
          runner = runner.next
          count += 1 

    if count < position:
       print ("requested position is invalid")
       return False
    else: 
        while runner:
            runner = runner.next
            current = current.next
        return current.data

# using recursion and print statement 
def find_kthto_last_recursion_1( head, position):
    if head == None:
        return 0 
    else:
        k = 1 + find_kthto_last_recursion_1(head.next, position)
        if k == position:
            print ("The number at position {} from end is {}" .format(position,head.data))
        return k 

# using recursion and wthout print statement 
class index:
      def __init__(self):
          self.value = 0

      def modify(self,i):
          self.value = i 
          pass 

def find_kthto_last_recursion(head, position):
    idx = index()
    node = find_kthto_last_recursion_2(head, position, idx)
    if node:
       return node.data
    else:
        return node

def find_kthto_last_recursion_2( head, position, idx):
    if head == None:
        return None 
    else:
        node = find_kthto_last_recursion_2(head.next, position, idx)
        idx.modify(idx.value + 1)
        if idx.value == position:
            return head
        else:
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
  print("enter the position from back of list ")
  position = int(input())
  
  """ 
  #print(find_kthto_last(l1.get_head(),position))

  # calling recursion function 
  list_len = find_kthto_last_recursion_1(l1.get_head(),position)
  if position > list_len :
      print ("requested position no is greater than lenght of list")
  """ 
 
  print(find_kthto_last_recursion(l1.get_head(),position))
