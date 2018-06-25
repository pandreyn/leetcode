"""
18. 4Sum
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
class Solution:
    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        if (nums is None or len(nums) < 4):
            return res

        nums = sorted(nums)
        n = len(nums)        

        for i in range(n - 3):
            if(nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target):
                break #first candidate too large, search finished
            if(nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target):
                continue #first candidate too small
            if (i != 0 and nums[i] == nums[i - 1]):
                    continue
            for j in range(i + 1, n - 2):   
                if(nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target):
                    break #second candidate too large
                if(nums[i] + nums[j] + nums[n - 1]+nums[n - 2] < target):
                    continue #second candidate too small             
                if (j != i + 1 and nums[j] == nums[j - 1]):
                    continue
                left = j + 1
                right = n - 1
                while (left < right):
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if (s == target):
                        res.append([nums[i], nums[j], nums[left], nums[right]])                        
                        left += 1
                        right -= 1
                        
                        while(left < right and nums[left] == nums[left + 1]):
                            left += 1
                        while(left < right and nums[right] == nums[right - 1]):
                            right -= 1
                    elif (s < target):
                        left += 1
                    else:
                        right -= 1


        return res
            
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
print(Solution().fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9))
print(Solution().fourSum([-1,0,1,2,-1,-4], -1))
print(Solution().fourSum([0, 0, 0, 0], 0))
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
