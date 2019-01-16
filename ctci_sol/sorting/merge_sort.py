
"""
time complexity : 
Merging : O(n):
    merging two sorted lists of length 'l' takes 
    The complexity of merge function is O(n),as it takes 2 arrays as an input,compare them and give output in new. As it is comparing 
    each element with every other element in the array,the complexity of this merge function comes out to be O(n)

We divide the list into two halves recursively. You can visualize it as a binary tree formed. Where height of this 
binary tree would be : (logn+1). Merging at each level takes O(n), total complexity takes (O(logn+1))*n) => O(nlogn)

The best, worst, average time compelxity of merge sort is O(nlogn)
"""

def merge_sort(lst):
    """Sorts the input list using the merge sort algorithm.
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
       elements one at a time.
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

if __name__ == "__main__":
   print ("hello")
   l1 = [10,2,20,1,30,-1]
   print ("sorted list is : ",merge_sort(l1))   
