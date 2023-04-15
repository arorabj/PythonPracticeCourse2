"""
Given a square matrix, turn it by 90 degrees in a clockwise

Input:
1 2 3
4 5 6
7 8 9

Output:
7 4 1
8 5 2
9 6 3

Input:
1 2
3 4

Output:
3 1
4 2
"""

input = [[1,2,3], [4,5,6], [7,8,9]]
#output = [[7,4,1], [8,5,2], [9,6,3]]

import copy
#
# def rotate_matrix(matrix):
#     # Step 1: transpose the matrix
#     n = len(matrix)
#     output=copy.deepcopy(input)
#     for i in range(n):
#         for j in range(i, n):
#             output[i][j] = matrix[j][i]
#             output[j][i]=  matrix[i][j]
#     # Step 2:reverse each row of the transposed matrix
#     for i in range(n):
#         output[i] = output[i][::-1]
#     return output
#
#
# input = [[1,2,3], [4,5,6], [7,8,9]]
# output = rotate_matrix(input)
# print(output)  # should print [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


a=[1,2,3,4,55,55,10,2,2,2,5]
b= set(a)
print (b)
l =list(b)
print (l[-2])
