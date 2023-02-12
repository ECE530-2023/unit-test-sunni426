# Write Function to multiply matrices
# Step 1: Write an empty function that its input are two matrices or vectors and it returns the output
# Step 2: Write test examples that will confirm your implementation based on the function defined in Step 1
# This includes wrong inputs, error conditions and correct output
# Step 3: Write matrix multiplication function

# To perform linting, open the Command Palette (⇧⌘P), filter on "linting", and select 
# Python: Run Linting. Linting will run automatically when you save a file.


import numpy as np
import tracemalloc
import cProfile, pstats
# import re
# cProfile.run('re.compile("foo|bar")')
import logging
import logging.config

# configuring logger
# create logger
logger = logging.getLogger('simpleExample')
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

# 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# # Logging to a file
# logging.basicConfig(filename='mat_multiply.log',level=logging.DEBUG)


'''
the above logging would produce the following output on the console:
2023-02-01 16:00:14,471 - simple_example - DEBUG - debug message
2023-02-01 16:00:14,471 - simple_example - INFO - info message
2023-02-01 16:00:14,471 - simple_example - WARNING - warn message
2023-02-01 16:00:14,471 - simple_example - ERROR - error message
2023-02-01 16:00:14,471 - simple_example - CRITICAL - critical message
'''


'''
Great for profiling:
https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/
https://docs.python.org/3/library/profile.html (CPU)
https://docs.python.org/3/library/tracemalloc.html (memory)

For logging:
https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial

'''


# # for debugging: add main function
# def main():
#     # store 5 frames
#     tracemalloc.start(5)

#     mat1 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3
#     mat2 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3
#     mat_multiply(mat1, mat2)

#     snapshot = tracemalloc.take_snapshot()
#     top_stats = snapshot.statistics('traceback')

#     # pick the biggest memory block
#     stat = top_stats[0]
#     print("%s memory blocks: %.1f KiB"%(stat.count,stat.size/1024))
#     for line in stat.traceback.format():
#         print(line)

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
        logger.error('Incorrect matrix input') # to console
        logging.error('Incorrect matrix input') # to log file
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
        logger.error('Dimension mismatch')
        logging.error('Dimension mismatch') # to log file
        raise ValueError("Dimension mismatch")

    for i in range(mat1_row):
        for j in range(mat2_col):
            for k in range(mat2_row):
                if ((type(mat1[i][k])==int or type(mat1[i][k])==float) and (type(mat1[i][k])==int or type(mat1[i][k])==float)):
                    mult_answer[i][j] += mat1[i][k]*mat2[k][j]
                else:
                    logger.error('Non-numerical input')
                    logging.error('Non-numerical input') # to log file
                    raise ValueError("Non-numerical input")

     
    return mult_answer


# mat1 = [[1,2,],[1,2,3],[1,2,3]] # 3 x 3
# mat2 = [[1,2,3],[1,2,3],[1,2,3]] # 3 x 3

# # store 5 frames
# tracemalloc.start(5) # start memory profiling
# # run
# mat_multiply(mat1, mat2)

# trace
# snapshot = tracemalloc.take_snapshot()

'''
Memory profiling


# top_stats = snapshot.statistics('traceback')
# # pick the biggest memory block
# stat = top_stats[0]
# print("%s memory blocks: %.1f KiB"%(stat.count,stat.size/1024))
# for line in stat.traceback.format():
#     print(line)
'''

# display the 10 files allocating the most memory
# top_stats = snapshot.statistics('lineno')
# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)
# print(f'Memory usage (bytes):{tracemalloc.get_tracemalloc_memory()}')


# profiler = cProfile.Profile()
# profiler.enable()
# mat_multiply(mat1,mat2)
# profiler.disable()
# stats = pstats.Stats(profiler).sort_stats('ncalls')
# stats.print_stats()
'''
output here:

    10 function calls in 0.000 seconds

    Ordered by: call count

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        1    0.000    0.000    0.000    0.000 mat_multiply.py:32(mat_multiply)

'''


# # debugging/tracing purposes
# if __name__ == '__main__':
#     main()