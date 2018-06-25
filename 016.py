"""
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        closest = None
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 2):
            start = i + 1
            end = n - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if closest == None or abs(target - closest) >= abs(target - s):
                    closest = s
                if s < target:
                    start += 1
                else:
                    end -= 1 

        return closest

print(Solution().threeSumClosest([-1, 0, 1, 2, -1, -4], 0))
print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
