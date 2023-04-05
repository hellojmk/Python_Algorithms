# Given k numbers which are less than n, return the set of prime number among them.
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Prime number : Natural numbers greater than 1 that has no positive divisors other than 1 and itself. (such as 2,3,5 ...)

n = 35

def primeNumber(x):
    
    # Empty list to store prime numbers
    result = []
    
    for num in range(x):
        # Check whether index is greater than 1 
        if num > 1:
            # range(start point, stop point)
            for i in range(2, num):
                # Check whether the number is divisible with number other than 1, which is not prime number
                if (num % i) == 0:
                    break
            else:
                result.append(num)
            
    return result

print(primeNumber(n))