

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def cal_power(x,n):
            if n == 0: 
               return 1.0
            val = cal_power(x,n/2)
            if n %2 == 0:
               return val*val
            else:
               return val*val*x
          
        if n < 0:
           x = 1/x
           n = n*-1
        return cal_power(x,n)


c1 = Solution()
print("----",c1.myPow(2,5))
