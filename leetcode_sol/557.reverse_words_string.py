
"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

class Solution(object):
    def reverse_word(self,word):
        if len(word) == 1:
           return word
        else:
           return word[-1] + self.reverse_word(word[:-1])
    
    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = ""
        
        for word in words:
            result = result + self.reverse_word(word) + " "
            
        return result[:-1]
        
