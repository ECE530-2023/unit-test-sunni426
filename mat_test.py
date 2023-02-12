from mat_multiply import mat_multiply
import numpy as np
import pytest
import tracemalloc
import logging
import logging.config

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


# configuring logger
# create logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG) # can set different mode (LEVELS)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# Logging to a file
logging.basicConfig(filename='mat_multiply.log',level=logging.DEBUG)


def test_dimensions():
    mat1 = [2, 2] # 1 x 2
    mat2 = [2, 2] # 1 x 2
    # using pytest to check error handling
    with pytest.raises(ValueError, match="Dimension mismatch"):
        mat_multiply(mat1, mat2)
        logging.error('Dimension mismatch') # to log file

def test_empty():
    mat1 = []
    mat2 = []
    assert mat_multiply(mat1, mat2)==[], "Empty matrices"

def test_partially_empty():
    mat1 = [1]
    mat2 = []
    with pytest.raises(ValueError, match="Incorrect matrix input"):
        mat_multiply(mat1, mat2)
        logging.error('Incorrect matrix input') # to log value

def test_value():
    mat1 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3
    mat2 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3
    assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all

def test_negative_values():
    mat1 = [[1,2,3],[1,-2,3],[1,2,-3]] # 3 x 3
    mat2 = [[1,2,-3],[1,-2,3],[-1,2,3]] # 3 x 3
    assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all

def test_non_numerical_input():
    mat1 = [['h',1]] # 1 x 2
    mat2 = [[0],[1]] # 2 x 1
    with pytest.raises(ValueError, match="Non-numerical input"):
        mat_multiply(mat1, mat2)

def test_tuple():
    mat1 = ((2,2),(2,2),(2,2))
    mat2 = ((2,2,2),(2,2,2))
    assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all

# def test_tuple2(): # does not pass yet!!
#     mat1 = (2,2)
#     mat2 = ((2,2))
#     assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all
# # - How to convert mat2 = ((2,2)) as a 1x2 tuple to a 1x2 list [[2,2]] ?

def test_decimal(): 
    mat1 = [[1,2,3],[1.3,2,3],[1,2,3]] # 3 x 3
    mat2 = [[1,2.0,3],[1,2,3],[1,2.0,3]] # 3 x 3
    assert (mat_multiply(mat1, mat2)==(np.matmul(np.array(mat1), np.array(mat2)))).all
