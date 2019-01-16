
# For given strings check is they are away from one edit or not
# One edit here means that one is string can be converted to another either by replace or adding or deletion of its element
#  Eg : pearls, pearl    ==> Ans : True 
#       pearls, bearls   ==> Ans : True
#       pearls, pearl    ==> Ans : True
#       pearls, parls    ==> Ans : True
#       pearls, bearl    ==> Ans : False

# Approach is to identify the above mentioned cases by observing mismstch    

def is_oneEdit_away(str1,str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1 == l2:
       return is_oneEdit_replace(str1,str2)
    elif l1 +1 == l2 :
       return is_oneEdit_insert(str1,str2)
    elif l1 -1 == l2:
       return is_oneEdit_insert(str2,str1)

    return False

def is_oneEdit_replace(str1,str2):
    
    mismatch_found = False 
    for index,i in enumerate(str1):
        if i != str2[index]:
           if mismatch_found:
              return False 
           else:
              mismatch_found = True
    return True

def is_oneEdit_insert(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    i = 0
    j = 0
    mismatch_found = False

    while i < l1 and j < l2:
          if str2[i] != str1[j]:
             if mismatch_found:
                 return False
             else:
                mismatch_found = True
                i += 1 
          else:
              i += 1
              j += 1

    return True


if __name__ == "__main__":
   print "hello"
   print "Enter first string"
   str1 = raw_input()
   print "Enter second string"
   str2 = raw_input()
   print is_oneEdit_away(str1,str2)


