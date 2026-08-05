'''

'''


class Solution(object):
    def countOdds(self, low, high):
        count = ((high +1)//2) - (low//2)
        return count
        