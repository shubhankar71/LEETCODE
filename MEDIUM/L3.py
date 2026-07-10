'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
'''


n = 120

def reverse(x):
    if x>=0:
        x= str(x)
        rev = int(x[::-1])
    else:
        x =str(x)
        rev = -1*int(x[::-1])
    if rev < (-2**31) or rev >(2**31-1):
        rev = 0
    return rev

print(reverse(n))
        