# Given an array nums, write a function to move all zeroes to the end of it, 
# while maintaining the relative order of the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def moveZero(x):
    
    for i in x:
        if i == 0:
            x.remove(i)
            x.append(i)
            
    return x

print(moveZero(array1))
print(moveZero(array2))
