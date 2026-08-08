''' 

'''

class Solution:
    def maximumGap(self, nums):
        maximum = 0
        nums.sort()
        for i in range(len(nums)-1):
            m = nums[i+1]-nums[i]
            maximum = max(maximum,m)
        return maximum