"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            left = i + 1
            right = n -1
            while (left < right):
                s = nums[i] + nums[left] + nums[right]
                if (s == 0):
                    res.append([nums[i], nums[left], nums[right]])
                    while(left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while(left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif (s < 0):
                    left += 1
                else:
                    right -= 1

        return res

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
