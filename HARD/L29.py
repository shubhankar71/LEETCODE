''''''

class Solution:
    def findMin(self, nums):
        nums.sort()
        return min(nums)