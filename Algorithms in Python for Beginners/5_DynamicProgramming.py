# Dynamic : A process or system characterized by constant change, activity or progress
# Principle of obtimality by
# - Breaking the problem down
# - Solving recursively
# - Use optimal solutions to construct optimal solutions

# 1. Ugly numbers
# Recursive function for successive divisions

def successive_div(x, y):
    while x % y == 0:
        x = x // y
    return x

# Function for checking if a number is ugly ot not
def ugly_check(num):
    num = successive_div(num, 2)
    num = successive_div(num, 3)
    num = successive_div(num, 5)
    
    if num == 1:
        return True
    else:
        return False

print(ugly_check(6))

# Function for finding the nth ugly number
def nth_ugly(n):
    i = 1
    # ugly number count
    counter = 1
    
    # Looping through all integers until ugly count becomes n
    while n > counter:
        i += 1
        if ugly_check(i):
            counter += 1
    return i
            
no = nth_ugly(100)
print("100th ugly number is", no)

# DP method : With DP 80% deduction

def nthUgly(n):
    dpUgly = [0] * n
    dpUgly[0] = 1

    u2 = u3 = u5 = 0

    multiple_2 = 2
    multiple_3 = 3
    multiple_5 = 5

    for i in range(1, n):
        dpUgly[i] = min(multiple_2, multiple_3, multiple_5)

        if dpUgly[i] == multiple_2:
            u2 += 1
            multiple_2 = dpUgly[u2] * 2

        if dpUgly[i] == multiple_3:
            u3 += 1
            multiple_3 = dpUgly[u3] * 3

        if dpUgly[i] == multiple_5:
            u5 += 1
            multiple_5 = dpUgly[u5] * 5

    return dpUgly[n - 1]

n = 15
print("15th ugly number is:", nthUgly(n))

# 2. TSP : Travelling Salesman Problem

from itertools import permutations
V = 4

def travel_salesman_problem(graph, s):
    # store all vertices
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
            #print(vertex)

    min_path = []
    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            #print(j, i, current_pathweight, graph[k][j])
            k = j
        current_pathweight += graph[k][s]
        min_path.append(current_pathweight)
        x = sorted(min_path)

    return x[0]

if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
    s = 0
    print(travel_salesman_problem(graph, s))
    
    # palindromic paths from top left to bottom right in a grid.

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# i and j are row and column indexes of top left corner (these are 0, 0) -- m and n are bottom right corner (4,3)

def palindromic_path(string, a, i, j, m, n):

    # See slides of path traversal - show as lists
    if j < m - 1 or i < n - 1:
        if i < n - 1:
            palindromic_path(string + a[i][j], a, i + 1, j, m, n)
        if j < m - 1:
            palindromic_path(string + a[i][j], a, i, j + 1, m, n)

    # If we reach bottom right corner (or end of the path), we go to is_palindrome function to check it.
    else:
        string = string + a[n - 1][m - 1]
        if is_palindrome(string):
            print(string)

a = [['a', 'a', 'a'],
     ['b', 'b', 'a'],
     ['a', 'b', 'a']]

str = ""
print(palindromic_path(str, a, 0, 0, 3, 3))