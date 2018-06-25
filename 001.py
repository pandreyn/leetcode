def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in dict:
                return (idx, dict[compliment])
            dict[num] = idx

def twoSum2(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       
        if len(nums) < 2:
            return None

        nums = sorted(nums)

        r = len(nums) - 1
        s = l =  0
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return (l, r)
            elif s < target:
                l += 1
            else:
                r -= 1

print(twoSum2([3, 2 ,4], 6))
print(twoSum2([2, 7, 11, 15], 9))
