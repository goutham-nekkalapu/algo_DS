
def max_product(nums):
    """
    time complexity : O(n), space O(1)
    """
    max_local = nums[0]
    min_local = nums[0]
    max_global = nums[0]
    
    for num in nums[1:]:
        max_local_temp = max(max(max_local*num, min_local*num),num)
        min_local_temp = min(min(max_local*num, min_local*num),num)
        max_global = max(max_local_temp,max_global)
        max_local = max_local_temp
        min_local = min_local_temp
    return max_global

if __name__ == "__main__":
   l1 = [-4,-3,-2]
   print(max_product(l1))
