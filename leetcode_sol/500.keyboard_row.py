
"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        rows = [['q','w','e','r','t','y','u','i','o','p'], ['a','s','d','f','g','h','j','k','l'], ['z','x','c','v','b','n','m']]        
        index = -1
        invalid_word_indexes = [] # holds indexes of invalid words
        
        for words_index,word in enumerate(words):
            if word[0].lower() in rows[0]:
                index = 0
            elif word[0].lower() in rows[1]:
                index = 1
            elif word[0].lower() in rows[2]:
                index = 2
                
            for letter in word[1:]:
                letter = letter.lower()
                if letter not in rows[index]:
                   invalid_word_indexes.append(words_index)
                   break
                    
        valid_words = [word for index,word in enumerate(words) if index not in invalid_word_indexes]
        return valid_words
        

## elagant way of doing :
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans=[]
        for word in words:
            t=set(word.lower())
            if a&t==t:
                ans.append(word)
            if b&t==t:
                ans.append(word)
            if c&t==t:
                ans.append(word)
        return ans 

