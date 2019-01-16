
# code to remove duplicates from an unsorted linkelist

# importing the linkedlist datastructure modules
import linkedlist as ll

# using a temporary buffer, a hash table
# Time complexity O(n)


def remove_duplicates(head):
    hash_map = {}
    prev = head  # head can not be the duplicate
    node = head
    while node:
        # checking if node's data already present in hash table
        if node.data in hash_map:
            prev.next = node.next
           # destroy(node)
        else:
            hash_map[node.data] = 1
            prev = node
        node = node.next
    pass

# without using any temprary buffer, but with two pointers
# Time complexity O(n^2) and space complexity O(1)


def remove_duplicates_1(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if current.data == runner.next.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    pass


if __name__ == "__main__":
    print("hello")
    print(" a single linked list ")
    l1 = ll.LinkedList()

    l1.add(10)
    l1.add(20)
    l1.add(30)
    l1.add(50)
    l1.add(60)
    l1.add(60)
    l1.print()
    node = l1.get_head()
    # remove_duplicates(node)
    remove_duplicates_1(node)
    l1.print()
