class Solution:
    def moveZeroes(self, nums):
        l = []
        for i in nums[:]:
            if i == 0:
                l.append(i)
                nums.remove(i)

        for j in l:
            nums.append(j)        