# Given a non-empty string s, you may delete at most one character. 
# # Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'
ss = 'apple'

def palindrome(x):
    for i in range(len(x)):
        # Using for loop, create 't' by following logic: SEQUENCE [START: STOP: STEP]
        # i = 0 / r + dkar = rdkar
        # i = 1 / ra + kar = rakar
        # i = 2 / rad + ar = radar (Can be True)
        # i = 3 / radk + r = radkr
        # i = 4 = radka = radka
        # i = 5 = radkar = radkar
        t = x[:i] + x[i+1:]
        
        # If t (after removing 1 character) is same as the reversed order t, then return true.
        if t == t[::-1]:
            return True
    
    return x == x[::-1]

print(palindrome(s))
print(palindrome(ss))