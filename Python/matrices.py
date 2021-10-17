#Write a program to add and multiply two matrices in python
import numpy as np

r, c = input("Enter the no of rows and columns : ").split()
r = int(r)
c = int(c)

print("Enter the first matrix : ",end='')
matrix1 = list(map(int, input().split()))
matrix1 = np.array(matrix1).reshape(r,c)
print(matrix1)

print("Enter the second matrix : ", end='')
matrix2 = list(map(int, input().split()))
matrix2 = np.array(matrix2).reshape(r, c)
print(matrix2)

matrix_add = np.add(matrix1,matrix2)
matrix_mul = np.dot(matrix1,matrix2)

print("The sum of the two matrices are : ",matrix_add,sep="\n")
print("The product of two matrices are : ",matrix_mul,sep="\n")
