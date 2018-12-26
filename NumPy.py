"""#NumPy Basic Concept   NumPy Cheatsheet"""

import numpy as nm
mylist = [1,4,6,7,8,14,9]
arr = nm.array(mylist)
#print(arr.shape)
arr1 = nm.array([[1,3,4], [5,6,7]])
#print(arr1)
print(nm.zeros((2,2)))
print(nm.ones((1,2)))
print(nm.full((2,2), 7))
print(nm.eye(3))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Array indexing~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
d = nm.array([[2,4,5],[4,6,7],[9,5,1]])
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
print(d[2:,1:3]) 
#Output [[5 1]]
print(nm.array([[1,4,5], [2,4,6],[7,8,9]], dtype = nm.float64))
print(nm.array([[1,4,5], [2,4,6],[7,8,9]]))
x = nm.array([[1,4,5], [2,4,6]], dtype = nm.float64)
y = nm.array([[0,5,6], [4,7,8]], dtype = nm.float64)
#Add two matrix
print(x + y) 
#Add two matrix
print(nm.multiply(x,y))
#Add Subtract matrix
print(nm.subtract(x, y))
#Add divide matrix
print(nm.divide(x, y))
#Add Sqare Root matrix
print(nm.sqrt(x))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""Note that unlike MATLAB, * is elementwise multiplication, not matrix multiplication.We instead use the dot function to compute inner products of vectors,
to multiply a vector by a matrix, and to multiply matrices. dot is available both as a function in the numpy module and as an instance method of array objects"""

x = nm.array([[1,2],[3,4]])
y = nm.array([[5,6],[7,8]])

v = nm.array([9,10])
w = nm.array([11, 12])


# Inner product of vectors; both produce 219
print(v.dot(w))
print(nm.dot(v, w))