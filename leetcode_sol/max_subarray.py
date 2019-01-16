
# prob : 53
 
def maxSubArray(nums):
    """
        :type nums: List[int]
        :rtype: int
    time compl : O(n)
    """ 
    max_global = nums[0]
    max_current = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current+num)
        if max_current > max_global:
           max_global = max_current 
    return max_global

def maxSubArray_indexes(nums):
    """
        :type nums: List[int]
        :rtype: int 
        returns max_subarray sum and the max sub array 
    time compl : O(n)
    """
    start_global = 0 
    end_global = 0 
    max_global = nums[0]
    max_current = nums[0]
    for index,num in enumerate(nums[1:]):
        if num > max_current+num and num > max_global:
           max_current = num
           max_global = num
           start_global = index
           end_global   = index
        elif max_current+num > max_global:
           max_current = max_current+num
           max_global = max_current
           end_global   = index
        else:
           max_current = max_current+num
    return max_global,[start_global,end_global]
         

if __name__ == "__main__":
   #l1 = [-2,1,-3,4,-1,2,1,-5,4]
   #l1 = [-2,1]
   l1 = [1]
   max_sum, indexes = maxSubArray_indexes(l1)
   print ("max sum is :",max_sum)
   print ("max sub array  is :",l1[indexes[0]:indexes[1]+1])
   max_sum = maxSubArray(l1)
   print ("max sum is :",max_sum)
              
           
             
