
#204 prime numbers < n 


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        complexity : nloglogn
        the method used is called : "Sieve of Eratosthenes"
        """
        is_prime = [True] *n
        i = 2 
        no_primes = 0
        while i < n:
              if is_prime[i]:
                  no_primes += 1
                  j = 2
                  while i*j < n:
                        is_prime[i*j] = False
                        j += 1
              i+= 1
        return no_primes
         
