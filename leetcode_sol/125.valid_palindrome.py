
"""
# question: 125
given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
    
Note: 
Have you consider that the string might be empty? This is a good question to ask during an interview.
        
For the purpose of this problem, we define empty string as valid palindrome.
"""

def is_palindrome(s):
    l, r = 0, len(s)-1

    while l < r:
        # moving forward into string till an aplha numeric is encountered
        while l < r and not s[l].isalnum():
            l += 1
        
        # from end moving into string till an aplha numeric is encountered
        while l <r and not s[r].isalnum():
            r -= 1
        # once aplhanumeric is encontered at front and at end, they are converted into lowercase and compared 
        if s[l].lower() != s[r].lower():
            return False

        # moving on to next locations 
        l +=1; r -= 1
    return True

if __name__ == "__main__":
  print("enter a string :")
  str1 = input()
  print(is_palindrome(str1))
