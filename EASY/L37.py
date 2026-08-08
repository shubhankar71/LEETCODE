'''

'''


import math
class Solution(object):
    def maxPairStrength(self, nums):
        m = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                f = nums[i]*nums[j]//(math.gcd(nums[i],nums[j])**2)
                m = max(m,f)
        return m
        