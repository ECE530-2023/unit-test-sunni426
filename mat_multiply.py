# Write Function to multiply matrices
# Step 1: Write an empty function that its input are two matrices or vectors and it returns the output
# Step 2: Write test examples that will confirm your implementation based on the function defined in Step 1
# This includes wrong inputs, error conditions and correct output
# Step 3: Write matrix multiplication function
 
import numpy as np

def mat_multiply(mat1, mat2):
    '''
    input() takes a string as input. "1 2 3"
    split() splits the string by whitespaces and returns a list of strings. ["1", "2", "3"]
    list(map(int, ...)) transforms/maps the list of strings into a list of ints. [1, 2, 3]
    '''
    
    # accepts list, sequence, or tuple form of matrix

    if (len(mat1)==0 and len(mat2)==0): # if empty matrix
        return []

    if (len(mat1)==0 or len(mat2)==0): # if empty matrix
        raise ValueError("Incorrect matrix input")

    # matrix 1: type processing & getting dimensions
    mat1_row = len(mat1)
    if type(mat1[0])==int or type(mat1[0])==float: # if mat1[0] is a singular element
        mat1_col = 1
    else:
        mat1_col = len(mat1[0])
    if type(mat1) is not list:
        mat1 = list(mat1) #[list(mat1)]

    # matrix 2: type processing & getting dimensions
    mat2_row = len(mat2)
    if type(mat2[0])==int or type(mat2[0])==float: # if mat2[0] is a singular element
        mat2_col = 1
    else:
        mat2_col = len(mat2[0])
    if type(mat2) is not list:
        mat2 = list(mat2) #[list(mat2)]

    mult_answer = np.zeros((mat1_row, mat2_col))
    if mat1_col!=mat2_row:
        raise ValueError("Dimension mismatch")

    for i in range(mat1_row):
        for j in range(mat2_col):
            for k in range(mat2_row):
                if ((type(mat1[i][k])==int or type(mat1[i][k])==float) and (type(mat1[i][k])==int or type(mat1[i][k])==float)):
                    mult_answer[i][j] += mat1[i][k]*mat2[k][j]
                else:
                    raise ValueError("Non-numerical input")

    # mult_answer = np.matmul(np.array(mat1),np.array(mat2)) # <class 'numpy.ndarray'>)
    # print(f'{mult_answer}\n')
    # print((np.matmul(np.array(mat1), np.array(mat2))))
    return mult_answer