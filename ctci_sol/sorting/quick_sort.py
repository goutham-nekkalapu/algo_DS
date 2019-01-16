
"""
time complexity : 
This is an example for divide and conquer method, recursion.
The average run time would be O(nlogn). As we divide the list to sublists recursively and each list takes O(n) to re-arrange according to
algorithm. So total we do it for O(logn) *n times => O(nlogn). 

Note that, here we are assuming that we choose the pivot in such a way that always we divide the list almost  near to the half.

Worst case would be : O(n^2) 
Best/average case = O(nlogn)
"""

# quick sort
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    # Start outside the area to be partitioned
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    # placing the pivot in b/w left and right lists
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    #return myList

# another way of implementing 'quicksort' algorithm 
def simple_quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Just use the + operator to join lists
        return simple_quicksort(less)+ equal+ simple_quicksort(greater)  
    else:  
        # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

if __name__ == "__main__":
   l1 = [7,2,5,1,29,6,4,19,11]
   quicksort(l1,0,len(l1)-1)
   print("sorted list is :", l1)

   l1 = [7,2,5,1,29,6,4,19,11]
   sorted_list = simple_quicksort(l1)
   print("sorted list is :", sorted_list)
