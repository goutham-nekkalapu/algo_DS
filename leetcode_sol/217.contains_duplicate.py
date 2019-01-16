

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    " time complex : O(n)
      space complex : O(n) --worst case 
      another approach is using sorting, time complexity : O(nlogn), space : O(n)
    """
    hash_map = {}
    for num in nums:
        if not num in hash_map:
           hash_map[num] = 1
        else:
           return True
    return False


if __name__ == "__main__":
   l1 = [1,2,3,4,2,5]
   print(containsDuplicate(l1))
