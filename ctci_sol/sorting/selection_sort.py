
"""
time complexity :
best case, worst case, average case = O(n^2)
no of times we iterate over the elements for comparision = n-1 + n-2 + n-3 + .....+1 = n*(n-1)/2. For asymptotic notation it becomes O(n^2)

"""

def selection_sort(l1):
    l = len(l1)

    for i in range(l):
        min_val = l1[i]
        for j in range(i+1,l):
            if l1[j] < min_val:
                min_val = l1[j]
                l1[j] = l1[i]
                l1[i] = min_val

if __name__ == "__main__":
   l1 = [10,2,20,1,30,-1]
   selection_sort(l1)
   print(" the sorted list is : ",l1)

