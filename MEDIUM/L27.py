class Solution:
    def search(self, nums, target):

        for i in range(len(nums)):
            if target == nums[i]:
                n = True
                break
            else:
                n = False
        return n
        