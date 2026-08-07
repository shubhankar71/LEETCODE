''''

'''

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxi = 0
        while left < right:
            nog = (right-left)*min(height[left], height[right])
            maxi = max(maxi, nog)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return maxi
