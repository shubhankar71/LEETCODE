'''
Unique Middle Element

You are given an integer array nums of odd length n.
Return true if the middle element of nums appears exactly once in the array. Otherwise return false.

 

Example 1:
Input: nums = [1,2,3]
Output: true
Explanation:
The middle element of nums is 2, which appears exactly once.
Thus, the answer is true.

Example 2:
Input: nums = [1,2,2]
Output: false
Explanation:
The middle element of nums is 2, which appears twice.
Thus, the answer is false.
'''



def isMiddleElementUnique(nums):
    s = nums.count(nums[(len(nums)-1)//2])   
    if s == 1:
        return True
    else:
        return False     
    
n = [1,2,2]

print(isMiddleElementUnique(n))