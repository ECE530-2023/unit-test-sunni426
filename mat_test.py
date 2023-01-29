from mat_multiply import mat_multiply
import numpy as np
import pytest

'''
Note: pytest will run all files of the form test_*.py or *_test.py in 
the current directory and its subdirectories

test cases (unit test):
- dimension mismatch
- empty matrices
- incomplete matrices
- non-numerical inputs
- input format
    - list
    - tuple
    - only separation by spaces, such as
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        1 1 1 1 1 1 1
- correct multiplication: 
    - positive numbers
    - negative numbers
    - 
'''

def test_dimensions():
    mat1 = [2, 2] # 1 x 2
    mat2 = [2, 2] # 1 x 2
    # using pytest to check error handling
    with pytest.raises(ValueError, match="Dimension mismatch"):
        mat_multiply(mat1, mat2)

def test_empty():
    mat1 = []
    mat2 = []
    assert mat_multiply(mat1, mat2)==[], "Empty matrices"

def test_partially_empty():
    mat1 = [1]
    mat2 = []
    with pytest.raises(ValueError, match="Incorrect matrix input"):
        mat_multiply(mat1, mat2)

def test_value():
    mat1 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3
    mat2 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3
    assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all

def test_negative_values():
    mat1 = [[1,2,3],[1,-2,3],[1,2,-3]] # 3 x 3
    mat2 = [[1,2,-3],[1,-2,3],[-1,2,3]] # 3 x 3
    assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all

def test_non_numerical_input():
    mat1 = ['h',1]
    mat2 = [0,1]
    with pytest.raises(ValueError, match="Non-numerical input"):
        mat_multiply(mat1, mat2)



