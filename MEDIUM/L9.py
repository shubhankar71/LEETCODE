'''
Sum of GCD of Formed Pairs

'''


import math
def gcdSum(nums):
    print(nums)
    prefixGcd = []
    mx =[]
    current_max =nums[0]
    
    for n in nums:
        if n>current_max:
            current_max=n
        mx.append(current_max)
    print(mx)
    
    for i in range(len(mx)):
        prefixGcd.append(math.gcd(nums[i],mx[i]))
    prefixGcd.sort()
    print(prefixGcd)
    
    new_preFGCD = []
    for i in range(len(prefixGcd)//2):
            m=prefixGcd[i]
            d=prefixGcd[len(prefixGcd)-1-i]
            new_preFGCD.append([m,d])           
    print(new_preFGCD)
    s = 0
    for sublist in new_preFGCD:
        a, b = sublist
        s += math.gcd(a,b)
        
    return s

        
    
    
n= [3,6,2,8]
print(gcdSum(n))
        
    
