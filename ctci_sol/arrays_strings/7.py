
# program to rotate a matrix by 90 degrees
# input is an n*n matrix 
# both the methods used work  without using swap memory

# rotate matrix/image 
class Solution(object):
    def rotate_90(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 1. first reverse the order of rows in input 2d list (i.e matrix)
        # 2. transpose the 2d matrix
        
        matrix.reverse()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
          for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
    def rotate_90_counter_clockwise(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 1. first reverse the order of columns in input 2d list (i.e matrix)
        # 2. transpose the 2d matrix
        # to understand try a 3x3 matrix 
       
        m = len(matrix) 
        n = len(matrix[0]) 
        
		#reversing the order of columns of the matrix  
        for l1 in matrix:
            for i in range(n/2):
                temp = l1[i]
                l1[i] = l1[n-1-i]
        
        for i in range(m):
          for j in range(i+1,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


# rotate input matrix by 90 degrees
def rotate_90(matrix):

    n = len(matrix)
    
    # checking if the matrix is NULL or not a square matrix 
    if n == 0 or n != len(matrix[0]):
       return None
     
    for layer in range(int(n/2)):
         first = layer
         last = n -1 -layer 
         for i in range(first,last):
             offset = i - first
             top = matrix[first][i]

             # moving left to top
             matrix[first][i] = matrix[last-offset][first]

             # moving bottom to left 
             matrix[last-offset][first] = matrix[last][last-offset]

             # moving right to bottom
             matrix[last][last-offset] = matrix[i][last]

             # moving top to right 
             matrix[i][last] = top

    return matrix

# rotate input matrix by -90 degrees
def rotate_minus_90(matrix):
    n = len(matrix)
    
    # checking if the matrix is NULL or not a square matrix 
    if n == 0 or n != len(matrix[0]):
       return None
     
    for layer in range(int(n/2)):
         first = layer
         last = n -1 -layer 
         for i in range(first,last):
             offset = i - first
             top = matrix[first][last-offset]

             # moving right to top
             matrix[first][last-offset] = matrix[last-offset][last]

             #moving bottom to right
             matrix[last-offset][last] = matrix[last][i]

             #moving left to bottom 
             matrix[last][i] = matrix[i][first]

             #moving top to left 
             matrix[i][first] = top

    return matrix


if __name__ =="__main__":
   
   # initilizing a matrix for testing 
   m = 4
   n = 4
   data = [[0 for i in range(n)] for j in range(m)]
   data[0] = [1, 2, 3, 4]
   data[1] = [5, 6, 7, 8]
   data[2] = [-1, -2, -3, -4]
   data[3] = [-5, -6, -7, -8]
   print(" the input matrix is : ")
   print (data)
   out = rotate_90(data)
   out = rotate_minus_90(data)

   if out == None:
       print(" The input matrix is either empty or not a square matrix")
   else:
       print(" the matrix rotated by 90 is :")
       print (out)
       
   out = rotate_minus_90(data)
   print(" the matrix rotated by -90 degrees is :")
   print (out)

