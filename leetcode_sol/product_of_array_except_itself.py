
# problem 238:

def productExceptSelf(nums):
    """
        :type nums: List[int]
        :rtype: List[int]
    time comp : O(n)
    space comp : O(n)
    """
    n = len(nums)
    temp_left = [1] *n 
    temp_right = [1] *n 
 
    # cal the prod of all elements present on left of its position 
    i = 1 
    while i < n:
          temp_left[i] = nums[i-1]*temp_left[i-1]
          i+= 1
  
    # cal the prod of all elements present on right of its position 
    i = n-2 
    while i >=0:
          temp_right[i] = nums[i+1]*temp_right[i+1]
          i-= 1

    # cal the prod of all elements present on its left,right of its position 
    i = n-2 
    i = 0  
    prod = [1] *n 
    while i<n:
          prod[i] = temp_left[i]*temp_right[i]
          i+= 1   
    return prod

def productExceptSelf_1(nums):
    """
        :type nums: List[int]
        :rtype: List[int]
    time comp : O(n)
    space comp : O(1); excluding the result 'prod' list 
    """
    n = len(nums)
    prod = [1] *n

    # cal the prod of all elements present on left of its position 
    i = 0
    temp = 1
    while i < n:
          prod[i] = temp
          temp *= nums[i]
          i+= 1

    # cal the prod of all elements present on left,right of its position 
    i = n-1
    temp = 1
    while i >=0:
          prod[i] = prod[i] * temp
          temp *= nums[i]
          i-= 1
    return prod

if __name__ == "__main__":
   l1 = [1,2,3,4,3]
   res = productExceptSelf(l1)
   res_1 = productExceptSelf_1(l1)
   print(res)
   print(res_1)
             

