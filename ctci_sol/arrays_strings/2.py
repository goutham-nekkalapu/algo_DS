
# program to check if a string is a permutation of other
# Assumptions:
#  1. Elements are encoded in ASCII format 
#  2. That same no of characters appear in the permuted string as well 
#     Eg : different, rentdiffe
#  3. Considering the words to be case sensitive. Eg : Abc != bca
#  4. White spacing is conidered to be valid 

def is_permutation(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        # array to keep track of character occurance; initilizing it with '0'
        l1 = [0] * 128
       
        for i in str1:
            index = ord(i)
            l1[index] += 1
      
        # decrementing the count of character occurance and checking of it is less than '0'
        for i in str2:
            index = ord(i)
            l1[index] -= 1
            if l1[index] < 0:
                return False

    return True


if __name__ == "__main__":
    print "hello"
    print "Enter the first string"
    str1 = raw_input() 
    print "Enter the second string"
    str2 = raw_input() 
  
    print is_permutation(str1,str2)
