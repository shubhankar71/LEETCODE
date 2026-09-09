
class Solution(object):
    def maxDigitRange(self, nums):
        max_range = -1
        answer = 0

        for num in nums:
            digits = str(num)

            largest = max(digits)
            smallest = min(digits)

            digit_range = int(largest) - int(smallest)

            if digit_range > max_range:
                max_range = digit_range
                answer = num

            elif digit_range == max_range:
                answer += num

        return answer