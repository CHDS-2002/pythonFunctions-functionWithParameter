# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')


# get_matrix - the function that creates the matrix
def get_matrix(n, m, value):
    # Creating a matrix
    matrix = [[value for _ in range(m)]
              for _ in range(n)]
    return matrix


# Let's create matrices
result1 = get_matrix(2, 2, 10)
# result1 - the first matrix
result2 = get_matrix(3, 5, 42)
# result2 - the second matrix
result3 = get_matrix(4, 2, 13)
# result3 - The third matrix

# ВЫВОД МАТРИЦ
print('\nMATRICES\n')
print('The first matrix:')
print(result1, end='\n\n')
print('The second matrix:')
print(result2, end='\n\n')
print('The third matrix:')
print(result3, end='\n\n')

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
