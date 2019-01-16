

def getSum(a, b):
    """
          :type a: int
          :type b: int
          :rtype: int
    """
    if a == 0 :
       return b 
    if b == 0:
       return a 
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    mask = 0xFFFFFFFF
    while b != 0 :              
          carry = a & b
          a = (a ^ b ) & mask 
          b = (carry << 1) & mask 

    if a <= MAX_INT:
  	   return a
    else:
       return ~((a%MIN_INT) ^ MAX_INT)

if __name__ == "__main__":
   #print(getSum(3,2))
   print(getSum(-1,-2))
