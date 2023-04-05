# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

#  eval() allows you to evaluate arbitrary Python expressions from a string-based or compiled-code-based input.

def addString(x, y):
    return str(eval(num1) + eval(num2))
               
print(addString(num1, num2))
print(type(addString(num1, num2)))