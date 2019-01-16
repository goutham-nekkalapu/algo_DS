
# prob: 153
#
def find_min(nums):
    n = len(nums)

    """
    if n == 1:
        return nums[0]
    elif n == 2:
         return nums[0] if nums[0] < nums[1] else nums[1]
    """
    
    start = 0 
    end = n-1
  
    while True:
        if end  < start:
            return nums[0]

        if end == start:
            return nums[start]

        mid = (start + end)//2

        if mid < end and nums[mid+1] < nums[mid]:
            return nums[mid+1]

        if mid > start and nums[mid] < nums[mid-1]:
            return nums[mid]

        if nums[end] > nums[mid]:
           end = mid-1

if __name__ == "__main__":
   #l1 = [10,-3,-2,-9,-6]
   l1 = [4,5,6,7,0,1,2]
   l1 = [-2,-3,0]
   l1 = [-1]
   l1 = [-2,-3]
   l1 = [-2,-5,-6,-12]
   print ("input is :",l1)
   print(find_min(l1))
