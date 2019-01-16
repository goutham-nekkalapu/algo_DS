
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # cal XOR of x and y 
        z = x^y
        hamming_dist = 0
        l1 = bin(z)
        for i in l1:
            if i == '1':
               hamming_dist += 1
        return hamming_dist
        
if __name__ == "__main__":
    s1 = Solution()
    print(s1.hammingDistance(1,4))
