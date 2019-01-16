

# using a different array Time and Memory O(n)  
def URLify(str1,length):
    l1 = ""
    for index,i in enumerate(str1):
        if index < length:
            if i == ' ':
               l1 = l1 + '%20'
            else:
               l1 = l1 + i 
    return l1

def URLify_1(str1,length):
    index = 0
    while (index < length):
          print "index = ",index
          if str1[index] == ' ':
             str1 = str1[:index] + '%20'+ str1[index+1:]
          else:
             index += 1
    return str1 

# to-do :  to be modified, verify once again for functionality    
""" 
def URLify_2(str2,length):
    print len(str2)
    no_spaces = 0 

    # calculating the  no of spaces
    for index,i in enumerate(str2):
        if index < length:
            if i == ' ':
                no_spaces += 1
    
    # estimating the new length of the string; inserting '%20' takes 3 places in string 
    new_len = length + no_spaces *2 

    # inserting the '%20' from back of string
    index = length
    new_index = new_len
    print new_index 
    str1 = list(str2)
    print str1
    while (index-1) >= 0   :
          print str1 [index-1]
          if str1[index-1] == ' ':
              str1[new_index-1] = '0'
              str1[new_index-2] = '2'
              str1[new_index-3] = '%'
              new_index -= 3
          else:
              str1[new_index-1] = str1[index-1]
          index -= 1
    return str1
"""

if __name__ == "__main__":
    print "hello"
    print "Enter a string in the following format:"
    print "string, actual length of string"
    print "   Eg: Mr John Smith    , 13 \n"
    str1, length = raw_input().split(',')
    #print URLify(str1,int(length)) 
    print URLify_1(str1,int(length)) 


