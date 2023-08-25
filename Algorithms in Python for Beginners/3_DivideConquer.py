# 1. Brute Force 
A = [-5,-23,5,0,23,-6,23,67]
C = []

while A:
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimum = x
    C.append(minimum)
    A.remove(minimum)

print(C)

# 2. Merge Sort - Optimized (LeetCode)
def merge_sort(nums):
    # Iterative merge sort using SORTED
    mid = len(nums)//2
    left = sorted(nums[:mid])
    right = sorted(nums[mid:])
    C = []
    
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] < right[0]:
            insert = left.pop(0)
            C.append(insert)
    
    if len(left) > 0:
        for i in left:
            C.append(i)
    
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C

arr = [9,8,7,6,5,4,3,2,1]
print(merge_sort(arr))

# 3. Matrix Multiplication
# m (rows) x n (columns)
# Numpy : Python library for multi-dimensional arrays

# Naive Method : Multiplying two matrices using nested loops

X = [[1, 2],
     [2, 3]]

Y = [[2, 3],
     [3, 4]]

result = [[0, 0],
          [0, 0]]

# Iterate through rows of X
for i in range(len(X)):
    # Iterate through colums of Y
    for j in range (len(Y[0])):
        # Iterate through rwos of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
        
        print(result)
        
# 4. Strassen Algorithm (Mindbreaker) : Using numpy and iteration
import numpy as np

x = np.array([[1,2],[2,3]])
y = np.array([[2,3],[3,4]])

def strassen_iter(x, y):
    
    # Splitting the mtrices into quandrants.
    a, b, c, d = x[0,0], x[0,1], x[1,0], x[1,1]
    e, f, g, h = y[0,0], y[0,1], y[1,0], y[1,1]
    
    # Computing the 7 products - This is where the magic happens...
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)
    
    # Computing the values of the 4 quadrants of the final matrix c
    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)
    
    return np.array([[c1, c2], [c3, c4]])

print(strassen_iter(x, y))

# 5. Strassen Algorithm (Mindbreaker) : Using numpy and recursion

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen_recur(x, y):
    
    # Check if the matrices are small enough for direct multiplication
    if x.shape[0] <= 2 or x.shape[1] <= 2:
        return np.dot(x, y)
    
    # Splitting the matrices into quadrants recursively
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    
    # Computing the 7 products, recursively 
    p1 = strassen_recur(a, f - h)
    p2 = strassen_recur(a + b, h)
    p3 = strassen_recur(c + d, e)
    p4 = strassen_recur(d, g - e)
    p5 = strassen_recur(a + d, e + h)
    p6 = strassen_recur(b - d, g + h)
    p7 = strassen_recur(a - c, e + f)
    
    # Computing the values of the 4 quadrants of the final matrix c
    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)
    
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically
    c = np.stack((np.hstack((c1, c2)), np.hstack((c3, c4))))
    
    return c

print(strassen_recur(x, y))