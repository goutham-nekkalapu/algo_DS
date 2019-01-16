
import collections 

class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        print("initial ans : ",ans)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            #print("count is : ", count)
            print ("--- ", tuple(count))
            ans[tuple(count)].append(s)
            print("ans ds is : ",ans)
        return ans.values()


if __name__ == "__main__":
   strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
   s1 = Solution()
   res = s1.groupAnagrams(strs)
   print ("the ans is :", res)
