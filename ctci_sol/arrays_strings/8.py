
# In a given MxN matrix, if one of the elements of row or coloumn are '0' populate the entire row and column with zeros

def populate_zeros(data):
    
    # finding if any first row or first column have zeros  
    row = 0
    col = 0

    for i in data[0]:
        if i == 0:
            row = 1
            break

    for x in data:
        if x[0] == 0:
            col = 1 
            break

    # visiting each node of matrix and using 0th row and col to keep track of rows and columns which have zeros
    for i,x in enumerate(data[1:],start =1):
        for j,y in enumerate(x[1:],start =1):
            if y == 0:
               data[0][j] = 0
               data[i][0] = 0
               break

    # poplulating the zeros in the matrix according to rule 
    for i,x in enumerate(data[1:],start =1):
        for j,y in enumerate(x[1:],start =1):
            if data[0][j] == 0 or data[i][0] == 0:
               data[i][j] = 0
   
    # if initially any element of first row or col is '0',now these are poplulated with zeros 
    if row == 1:
       x = data[0]
       for i,val in enumerate(x):
             data[0][i] = 0
    
    if col == 1:
       for i,x in enumerate(data):
            data[i][0] = 0

    return data

if __name__ =="__main__":
    # initilizing a matrix for testing 
    m = 4 
    n = 4
    data = [[0 for i in range(n)] for j in range(m)]
    data[0] = [1, 9, 3, 5]
    data[1] = [1, 2, 0, 4]
    data[2] = [1, 0, 2, 4] 
    data[3] = [1, 3, 6, 7]

    out = populate_zeros(data)
    print ("modified matrix is :",out)
    
