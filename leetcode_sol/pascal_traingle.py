

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
          return []
        
        res = [[1]]
        row = [1]
        for index in range(numRows):
            for l in zip([0]+row, row+[0]):
                print(index+1,"---",l) 
            row = [x + y for x, y in zip([0]+row, row+[0])]
            print("***",row)
            res.append(row)
        return res


if __name__ == "__main__":
  s1 = Solution()
  res = s1.generate(3)
  print(res) 
