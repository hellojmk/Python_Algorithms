# 1. Reverse Integer
# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverseInteger(x):
    # Convert integer x into string
    x_str = str(x)
    # Container for reversed integer 
    result = 0

    # Check whether index 0 consists of negative sign
    if x_str[0] == '-':
        # To display the 1st element to last element in steps of 1 in reverse order, 
        # we use the [::-1]. The [::-1] reverses the order
        # [:0:-1] means it stops slicing the array in reverse order at index 1 (index 0 excluded)
        result = int('-' + x_str[:0:-1])
    else:
        result = int(x_str[::-1])
    
    return result

print(reverseInteger(12345))
print(reverseInteger(-123))            

