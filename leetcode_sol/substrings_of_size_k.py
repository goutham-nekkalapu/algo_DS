

def distinct_substrigns(str1, k):
    """
    returns all possible substrings of size 'k', where all the char in substring are distinct 
    """
    hash_map = {}
    n = len(str1)
    start = 0 
    end = 1
    hash_map[str1[start]] = 1
    res = [] 

    while end < n:
        print ("hash_map is :", hash_map)
        if str1[end] not in hash_map: 
           hash_map[str1[end]] = 1
        else:
           while str1[start]!=str1[end]:
                 del hash_map[str1[start]]
                 start += 1
           start += 1

        if end-start+1 == k:
           temp = str1[start:end+1]
           if temp not in res:
              res.append(temp)
           del hash_map[str1[start]]
           start += 1
        end += 1
        #print(end,start)
    return res 


if __name__ == "__main__":
   print("enter a string")
   str1 = input()
   print("enter the value of k")
   k = int(input())
   res = distinct_substrigns(str1,k)
   print("the res is : ", res)
