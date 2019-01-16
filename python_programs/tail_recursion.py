
# This program gives two versions of recursion. Tail and non-tail recursion
# Tailed recurison is best as the modern day compilers would optimize them, eliminating the recurison part ( thus helps us by eliminating 
# the need to store the stack pointers for each function call ). Typically compilers use 'goto' statement to achieve this
#
#  Here we will see a factorial cal problem in both the versions  
#

def recursion_tailed(n, a):
    print "a is",a
    print "n is",n
    if n == 0:
        return a 
    else:
        return recursion_tailed(n-1,n*a)

def recursion(n):
    if n == 1:
        return 1;
    else:
        return n*recursion(n-1)

if __name__ == "__main__":
   print recursion_tailed(1000,1)
   #print recursion(1000)
