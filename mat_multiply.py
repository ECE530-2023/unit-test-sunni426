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
    if type(mat1) is not list:
        mat1 = list(mat1)
    mat1_row = len(mat1)
    if type(mat1[0]) is not list: # if mat1[0] is a singular element
        mat1_col = 1
    else:
        mat1_col = len(mat1[0])

    # matrix 2: type processing & getting dimensions
    if type(mat2) is not list:
        mat2 = list(mat2)
    mat2_row = len(mat2)
    if type(mat2[0]) is not list: # if mat2[0] is a singular element
        mat2_col = 1
    else:
        mat2_col = len(mat2[0])

    # print(f'mat1_row: {mat1_row}')
    # print(f'mat2_row: {mat2_row}')
    # print(f'mat1_col: {mat1_col}')
    # print(f'mat2_col: {mat2_col}')

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
    print(f'{mult_answer}\n')
    print((np.matmul(np.array(mat1), np.array(mat2))))
    return mult_answer








# # Write Function to multiply matrices
# # Step 1: Write an empty function that its input are two matrices or vectors and it returns the output
# # Step 2: Write test examples that will confirm your implementation based on the function defined in Step 1
# # This includes wrong inputs, error conditions and correct output
# # Step 3: Write matrix multiplication function

# import numpy as np

# '''
# 1) get user input for dimensions: user enter format: row, col. enter. row, col
# 2) check if matrix multiplication rules work (dimension match). if not, raise error. o/w, proceed
# 3) get user input for matrix: exammple format entry
#     prompt: please enter first matrix.
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1

#         1 1
#         1 1
#     prompt: please enter second matrix.
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1
#         1 1 1 1 1 1 1
# 3) check if are numbers, and if input dimensions correspond to given dimensions
# 4) if so, do matrix mult. otherwise, raise error

# '''

# # class Matrix:
# #     def __init__(self, mat1_row, mat1_col, mat2_row, mat2_col):
# #         self.mat1_row = mat1_row
# #         self.mat1_col = mat1_col
# #         self.mat2_row = mat2_row
# #         self.mat2_col = mat2_col

# #     def getInput():
#         # mat1_row = input("Enter # of rows in matrix 1: ")


# def mat_multiply():
#     mat1_row = input("Enter the number of rows in matrix 1: ")
#     mat1_col = input("Enter the number of columns in matrix 1: ")
#     mat2_row = input("Enter the number of rows in matrix 2: ")
#     mat2_col = input("Enter the number of columns in matrix 2: ")

#     # check if dimensions are integers
#     # if !mat1_row.isdigit() || !mat1_col.isdigit() 
#     #     || !mat2_row.isdigit()||!mat2_col.isdigit():


#     # check if matrix mul. rules are satisfied (mat1_col == mat2_row)


#     # get user matrix
#     # initialize matrix
#     mat1 = []
#     mat2 = []

#     print("1st matrix, enter the entries rowwise: ")
#     for i in range(int(mat1_row)):          # A for loop for row entries
#         a =[]
#         for j in range(int(mat1_col)):      # A for loop for column entries
#             a.append(float(input()))
#         mat1.append(a)


#     print("2nd matrix, enter the entries rowwise: ")
#     for i in range(int(mat2_row)):          # A for loop for row entries
#         b = []
#         for j in range(int(mat2_col)):      # A for loop for column entries
#             b.append(float(input()))
#         mat2.append(b)


#     print(f'mat1 is \n {mat1}\n')
#     print(f'mat2 is \n {mat2}\n')

#     mult_answer = np.matmul(np.array(mat1),np.array(mat2))
#     print(f"answer: \n{mult_answer}")


# mat_multiply()



# # test cases

# # a possible unit test: checking empty matrices









# Write Function to multiply matrices
# Step 1: Write an empty function that its input are two matrices or vectors and it returns the output
# Step 2: Write test examples that will confirm your implementation based on the function defined in Step 1
# This includes wrong inputs, error conditions and correct output
# Step 3: Write matrix multiplication function

import numpy as np

'''
1) get user input for dimensions: user enter format: row, col. enter. row, col
2) check if matrix multiplication rules work (dimension match). if not, raise error. o/w, proceed
3) get user input for matrix: exammple format entry
    prompt: please enter first matrix.
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1

1 1
1 1
    prompt: please enter second matrix.
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
3) check if are numbers, and if input dimensions correspond to given dimensions
4) if so, do matrix mult. otherwise, raise error

'''

# class Matrix:
#     def __init__(self, mat1_row, mat1_col, mat2_row, mat2_col):
#         self.mat1_row = mat1_row
#         self.mat1_col = mat1_col
#         self.mat2_row = mat2_row
#         self.mat2_col = mat2_col

#     def getInput():
        # mat1_row = input("Enter # of rows in matrix 1: ")


# def mat_multiply():
#     '''
#     input() takes a string as input. "1 2 3"
#     split() splits the string by whitespaces and returns a list of strings. ["1", "2", "3"]
#     list(map(int, ...)) transforms/maps the list of strings into a list of ints. [1, 2, 3]
#     '''
    
#     mat1_row = int(input("Enter the number of rows in matrix 1: "))
#     mat1_col = int(input("Enter the number of columns in matrix 1: "))
#     # mat2_row = input("Enter the number of rows in matrix 2: ")
    

#     # check if dimensions are integers


#     # check if matrix mul. rules are satisfied (mat1_col == mat2_row)

#     i = 0
#     mat1 = [list(map(int,input(f"Enter row {i}: ").split())) for i in range(mat1_row)]     
#     print(mat1)

#     mat2_row = int(input("Enter the number of rows in matrix 2: "))
#     mat2_col = int(input("Enter the number of columns in matrix 2: "))

#     i = 0
#     mat2 = [list(map(int,input(f"Enter row {i}: ").split())) for i in range(mat2_row)]     
#     print(mat2)

#     # print(f'\n{mat1}')

#     mult_answer = np.zeros((mat1_row,mat2_col))

#     for i in range(mat1_row):
#         for j in range(mat2_col):
#             for k in range(mat2_row):
#                 mult_answer[i][j] += mat1[i][k]*mat2[k][j]

#     # mult_answer = np.matmul(np.array(mat1),np.array(mat2)) # <class 'numpy.ndarray'>)
#     print(f'{mult_answer}')
#     # return mult_answer


# mat_multiply()