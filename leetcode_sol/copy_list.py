


import random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        
        node = head 
        new_list = temp = RandomListNode(-1)
        new_list_add = []
                
        while node != None:
            new_node = RandomListNode(node.label)
            temp.next = new_node
            new_list_add.append(new_node)
            node = node.next

        temp =  new_list.next   
        while temp!= None:
              temp.random = random.choice(new_list_add)
              temp = temp.next
            
        return new_list.next

if __name__ == "__main__":
   
