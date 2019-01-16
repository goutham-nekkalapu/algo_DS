
class ListNode(object):
      def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

def print_list(head):
    temp = head
    while temp:
          print(temp.val)
          temp = temp.next 

if __name__ == "__main__":
   head = ListNode(10)
   n2 = ListNode(20)
   n3 = ListNode(30) 
   n4 = ListNode(40) 
   head.next = n2
   n2.next = n3
   n3.next = n4
  
   print("before") 
   print_list(head) 
   s1 = Solution()
   res = s1.removeNthFromEnd(head,1)
   print("end") 
   print_list(res) 
   
