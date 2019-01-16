

def fibonacci(n):
    memo = [0]*(n+1) #array to memoize the results in each step 
    memo[0], memo[1] = 0,1
    for i in range(2,n+1):
        memo[i] = memo[i-2] + memo[i-1]
    return memo[n]


if __name__ == "__main__":
   print("enter the number to be found in a fibonacci series")
   n = int(input())
   print("-- ",fibonacci(n))
