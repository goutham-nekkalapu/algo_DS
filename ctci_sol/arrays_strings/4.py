
# program to check if given string is a permutation of a pallindrome   
# If it is a pallindrome then only atmost one element of string can occur odd no of times. 


# assuming the string is ASCII encoded, calculating the occurance of each elements and storing them  
# complexity : O(n+k) time and O(k) space 

def is_pallnd(str1):
    # array to keep track of character occurance; initilizing it with '0'
    l1 = [0] * 128

    for i in str1:
        index = ord(i)
        l1[index] += 1

    # checking for occurance of odd appearance of multiple elements 
    count = 0 
    for i in l1:
        if i%2 == 1:
           count += 1

        if count > 1:
           return False
    return True

# inorder to improve space complexity can use bitvector. For every occurance of an element we add '1' to that corresponding element. 
# So, for even occurance of an element it will have '0' at its corresponding posistion and for odd occurances '1'. 
# To verify that only there is single occurance of '1' in vector ( for it be pallindrome) we can that by subtracting 1 from that and performing
# 'AND' operation to that. If it is '0' it has only one '1' else multiple '1' 

def using_bit_vector(str1):
# how to create bitvectors in python and perform bitwise operations on them ?

    pass 

if __name__ == "__main__":
    print ("please enter a string")
    str1 = input()
    print (is_pallnd(str1))
    #using_bit_vector(str1)
