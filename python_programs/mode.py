
import numpy as np

# using numpy's bincount function 
def calmode_using_numpy1(l1):
    counts = np.bincount(l1)
    return np.argmax(counts) 

# using numpy's unique() function
def calmode_using_numpy2(l1):
    (values,counts) = np.unique(l1,return_counts=True)
    ind=np.argmax(counts)
    return (values[ind])

# using dictionary 
def calmode_using_dict(l1):
    list_dict = {}
    for i in l1:
        if i in list_dict:
            list_dict[i] += 1
        else:
            list_dict[i] = 1 
    return sorted(list_dict, key=list_dict.get, reverse=True)[0]


if __name__ == "__main__":
   print ("Enter a list of integers whose mode you wish to find ")
   print ("Enter the list with space seperation ")
   print ("Eg : 1 2 2 4 5 4 6 5")
   print ("\n")
   print ("Please enter below : ")

   l1 = input()
   l1 = l1.split(" ")
   l1 = list(map(int, l1)) # converting the input from string to integer 

   print ("The mod of given array is : ",calmode_using_dict(l1))
   # print ("The mod of given array is : ",calmode_using_numpy1(l1))
   # print ("The mod of given array is : ",calmode_using_numpy2(l1))

"""
If the input is any other format other than integer, Eg: Text, where we are trying to find out the word that occurs the most in a text then,
'calmode_using_dict()', can be used. But for this just comment the line:35 
"""


