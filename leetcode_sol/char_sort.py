
from collections import Counter

def frequencySort(s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = Counter(s), {}
        for k,v in c1.items():
            c2.setdefault(v, []).append(k*v)
        print ("----",c1)
        print ("---c2 is ",c2)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])


if __name__ == "__main__":
   s = "kumarkuma"
   print(frequencySort(s))
   
