
"""
time complexity: O(n^2) 

"""

def bubble_sort(l1):
    l = len(l1) 
    while l >1:
          count = 0 # gives no of swaps done if no swaps => list sorted   
          for i in range(l-1):
              # bubbling the greater element to right of list
              if l1[i] > l1[i+1]: 
                 temp = l1[i+1]
                 l1[i+1] = l1[i]
                 l1[i] = temp
                 count += 1 
          if count == 0:
             return 
          else:
             l -= 1 # reducing the length of the list as right most elements are already sorted  

if __name__ == "__main__":
   l1 = [1,3,2,10,-1,5]
   bubble_sort(l1)
   print("sorted list is :",l1)
