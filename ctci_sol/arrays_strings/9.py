
# Given two strings s1, s2. We need to check if s2 is a rotation of s1 using only one call of issubstring() function. 
#
# Eg : given that 
#               s1 = "waterbottle"
#               s2 = "erbottlewat"
#
#      Here s2 is a rotation of s1 rotated after 'wat'. 
#      for clear understanding, consider x = "wat", y = "erbottle";  s1 = xy and s2 = yx


# funciton to find the if s2 is a substring of s1
def is_substring(s1,s2):
   
    i = 0
    l = len(s2)-1
    
    # traversing through the string s1
    for ch in s1:
        if ch == s2[i]:
           if i==l:
              return True
           else:
              i += 1
        else:
            i = 0

    return False


if __name__ == "__main__":
    print ("Enter the strings s1 and s2 to verify of s2 is a rotation of s1 ")
    s1 = input()
    s2 = input()
  
    l1 = len(s1)
    if l1 == len(s2) and l1 > 0:
       new_s1 = ""
       new_s1 = s1+s1
       print(is_substring(new_s1,s2))
    else:
       print("False")

