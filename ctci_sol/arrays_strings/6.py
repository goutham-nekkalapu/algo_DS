

# Forming a string with the no of consequetive occurances of each character; if formed string length is less than input return orignal
#  Eg 1 : input  : aaabbcceee
#         output : a3b2c2e3
#
#  Eg 2 : input      : aaabcdef 
#         compressed : a3b1c1e1f1 
#         output     : aaabcdef
#
#  Sol time complexity is O(n)

def compress(str1):
    # compressed string 
    str_comp = []
    prev = str1[0]
    count = 1

    # traversing the string and checking current element with the perv element O(n)
    for i in str1[1:]:
        if i == prev:
            count += 1 
        else:
            str_comp.append(prev)
            str_comp.append(count)
            count = 1
            prev = i 
    str_comp.append(prev)
    str_comp.append(count)

    # converting to string O(n)
    out = ''
    out = ''.join(str(x) for x in str_comp)
    
    if len(out) > len(str1):
        return str1 
    else:
        return out

if __name__ == "__main__":
    print ("Enter a string :")
    str1 = input()
    print ("compressed output is :",compress(str1))


