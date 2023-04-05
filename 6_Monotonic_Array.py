# Given an array of integers, determine whether the array is monotonic or not.
# Monotonic Array : An array is monotonic if it is either monotone increasing or monotone decreasing. 
# An array nums is monotone increasing if for all i <= j , nums[i] <= nums[j] . 
# An array nums is monotone decreasing if for all i <= j , nums[i] >= nums[j] .

# all() : The all() function returns True if all items in an iterable are true, otherwise it returns False.
# all() : If the iterable object is empty, the all() function also returns True.

A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def monotonicArray(x):
    return (all(x[i] <= x[i + 1] for i in range(len(x) - 1))
            or all(x[i] >= x[i + 1] for i in range(len(x) - 1)))

print(monotonicArray(A))
print(monotonicArray(B))
print(monotonicArray(C))