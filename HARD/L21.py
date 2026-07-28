'''
Median of Two Sorted Arrays.

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l = []
        m = max(len(nums1),len(nums2))
        for i in nums1:
            l.append(i)
        for i in nums2:
            l.append(i)
        l.sort()
        if len(l)%2==1:
            return float(l[len(l)//2])
        else:
            n = (l[len(l)//2]+ l[(len(l)//2)-1])/2.0
            return n

        
