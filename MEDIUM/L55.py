class Solution(object):
    def maxValidPairSum(self, nums, k):
        n = len(nums)

        max_i = nums[0]
        ans = float('-inf')

        for j in range(k, n):
            # nums[j-k] has now become a valid i
            max_i = max(max_i, nums[j-k])

            # Best valid i + current j
            ans = max(ans, max_i + nums[j])

        return ans