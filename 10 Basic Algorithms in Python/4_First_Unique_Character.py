# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. 
# Note: all the input strings are already lowercase.

# Solution 1.
def firstUnique_1(x):
    # We use dictionary as word container, because of counting characters from string data.
    # If we use list, list indices must be integers, not str. So, we can not use list in this case.
    frequency = {}
    
    # For loop through the word (parameter x)
    for i in x:
        # If the each character is not in frequency dict, set value 1 according to the each key.
        if i not in frequency:
            frequency[i] = 1
        # If the each character is already in frequency dict, increment 1, so that we can detect the character is not unique.
        else:
            frequency[i] += 1
    
    # For loop through the length of word (parameter x)
    for i in range(len(x)):
        # Find the FIRST unique character in freqeuncy dict.
        if frequency[x[i]] == 1:
            return i
    return -1

print(firstUnique_1('alphabet')) # l is fist unique character. Answer # 1
print(firstUnique_1('barbados')) # r is fist unique character. Answer # 2
print(firstUnique_1('crunchy')) # r is fist unique character. Answer # 1


# Solution 2. Use Counter() from collections library
import collections
def firstUnique_2(x):
    
    # Build hash map : Each character and each appearance
    count = collections.Counter(x) # <-- gives back a dictionary with words occurrence count 
                                         #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    
    # Find the first unique index
    for idx, ch in enumerate(x):
        if count[ch] == 1:
            return idx
    return -1

print(firstUnique_1('alphabet')) # l is fist unique character. Answer # 1
print(firstUnique_1('barbados')) # r is fist unique character. Answer # 2
print(firstUnique_1('crunchy')) # r is fist unique character. Answer # 1