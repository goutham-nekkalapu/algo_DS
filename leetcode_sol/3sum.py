

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []      
        n = len(nums)
        
        if n < 3:
          return []
        print ("----")
 
        index = 1 
        while index < n-1:
          print("index is :",index)
          start = 0
          while start < index:
            temp = [nums[start], nums[index], nums[index+1]]
            if sum(temp) == 0 and temp not in res:              
              res.append(temp)
            start += 1
          index += 1
            
        return res
       

if __name__ == "__main__":
   nums = [0,0,0]
   a1 = Solution()
   res = a1.threeSum(nums)
   print ("res is :",res) 
   res1 = set(res)
   print ("res1 is :",res1)
   res1 = list(res1)
