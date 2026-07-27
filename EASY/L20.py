'''

'''


class Solution(object):
    def arraySign(self, nums):
        x = 1
        for i in range(len(nums)):
            x = x*nums[i]
        if x>0:
            return 1
        elif x<0:
            return -1
        else:
            return 0
        