
# Given an array containing None values fill in the None values with most recent non None value in the array 
# In this case, most recent values in the value is the value right before the None value.

array1 = [1, None, 2, 3, None, None, 5, None]

def fillBlank(x) :
    
    # Empty list to store new values
    result = []
    # Define valid as 0 first and the nupdate valid as i, if it is not None
    valid = 0
    
    # Collect NOT None values first
    for i in x :
        if i is not None:
            result.append(i)
            valid = i
        else:
            result.append(valid)
            # No statement for updating valid, because we need to use the former index to fill in None values
            
    return result

print(fillBlank(array1))