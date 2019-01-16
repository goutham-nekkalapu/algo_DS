
# this program prints all the powers of 'm' b/w 1 to 'n'
# Eg: n = 10, m = 2 output : 1, 2, 4, 8  
#
#


if __name__ == "__main__":
    print "hello"

    flag = True
    while (flag):
        print "\nEnter a number which you want to check"
        n = int (raw_input())
        print "Enter a base number which you want to check"
        m = int (raw_input())
        if m > n:
             print "The base is greater than the no, try agian"
        elif m == 0:
             print "The base value entered is '0', try agian"
        else :
             flag = False
 
    i = 1 
    print "the power of m b/w 0 and {} are :".format(n) 
    while (i <= n):
         #print (i, end='')
         print i,
         i = i * m 
          
