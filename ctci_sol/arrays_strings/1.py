
# Here I am assuming that each element in string is encoded in ASCII format  

# using data structure 
def is_unique(str_1):

    # a boolean array which keeps track of unique characters, initialized to zero
    l1 = [0] * 128
   
    # if the length of the string is greater than 128 (max possible for ASCII encoding)
    if len(str_1) > 128:
        return False

    # for each element in string checking with boolean array
    for i in str_1:
        index = ord(i)
        if l1[index] == 1:
            return False
        else:
            l1[index] = 1

    return True

# using data structure : dictionary 
def is_unique_dict(str_1):
    # create a boolean dictionary of all characters first with values of True 
    # then iterate over the string to find False if not unique 

    return 

# if no data structures are to be used
# can check using brute force TC = O(n^2) 
# using sorting : O(nlogn + n) 

def is_unique_no_ds(str_1):

    # sorting the given string : O(nlogn) 
    str_1 = ''.join(sorted(str_1))

    prev = ord(str_1[0]) 

    # comparing the ASCII values of previous element to present one : O(n)
    for i in str_1[1:]:
        current = ord(i)
        if prev == current:
           return False
        else:
           prev = current 
     
    return True


if __name__ == "__main__":
    str_1 = raw_input()

    # using data structure method 
    print is_unique(str_1)
  
    # without using any DS 
    print is_unique_no_ds(str_1)


