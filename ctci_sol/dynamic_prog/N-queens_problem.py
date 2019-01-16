
"""
solving N-Queen's problem using backtracking 
"""

def column(board, i):
    """
    returns column from a square matrix 
    """
    return [row[i] for row in board]

def is_attacked(x, y, board ):
    """
    return 'True' if x,y location on board is is_attacked by 
    previously existing Queens else return 'False' 
    """
    # checking at row and column  
    row = board[x]
    for val in row:
        if val == 1:
           return True 
    
    col = column(board,y)
    for val in col:
        if val == 1:
            return True

    # getting the dimensions of board 
    n = len(board[0]) 
    
    #checking the diagonal values of x,y
    for i in range(n):
        for j in range(n):
            if i+j == x+y or i-j == x-y:
                if board[i][j] == 1:
                    return True 
    return False 

def create_board(N):
    """
    creates an NxN board and intializes value at each square as '0' 
    """
    board = [[0 for x in range(N)] for y in range(N)] 
    return board  

def print_board(board):
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print("")

def solve(board, N):
    """
    returns 'True' if Queens can be placed else 'False'
    """
    # when all the N queens are placed 
    if N == 0:
       return True

    # cal dimension of board 
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            attacked = is_attacked(i, j, board) # checking if (i,j) is safe to place the queen 
            if attacked == False:
               board[i][j] = 1   # place the queen at location (i,j)
               if solve(board, N-1): # proceed ahead with placing other queens 
                    return True
               else:
                   board[i][j] = 0   # if could not place all the queens, changing our decision and
                                     # moving to other positions 
    return False

def N_queens_prob(N):
    board = create_board(N)
    result = solve(board, N)
    return result, board

# execution starts here 
if __name__ == "__main__":
   print ("enter the value of N ")
   N = int(input())
   result, board = N_queens_prob(N)
   print (result)
   print_board(board)
