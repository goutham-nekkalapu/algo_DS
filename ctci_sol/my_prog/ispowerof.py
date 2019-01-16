
# this program find if a given no 'n' is a power of no 'm'
# Eg : 
#     n = 8, m = 2 output : yes
#     n = 10, m =2 output : No  
#


if __name__ == "__main__":

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

    flag = True
    n_orig = n 
    while(flag):
         if n%m != 0:
             print "{} is not a power of {}".format(n_orig,m)
             flag = False 

         elif n/m == 1:
             print "{} is a power of {}".format(n_orig,m)
             flag = False 

         else :
              n = n/m

              


