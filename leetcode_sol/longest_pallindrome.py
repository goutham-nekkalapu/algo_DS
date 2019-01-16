


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            print ("the val of i :", i)
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
      
      # get the longest palindrome, l, r are the middle indexes   
      # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
              l -= 1; r += 1
        print("--- ",s[l+1:r])
        return s[l+1:r]


if __name__ == "__main__":
   print("enter ur string")
   str1 = input()
   s1 = Solution()
   res = s1.longestPalindrome(str1)
   print ("the longest substring that is a pallindrome is : ",res)
