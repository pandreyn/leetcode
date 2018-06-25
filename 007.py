"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2 ** 31,  2 ** 31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        negative = x < 0
        if negative:
            x = 0 - x

        if x > 2 ** 31 - 1:
            return 0

        res = 0
        while x > 0:            
            rest = x % 10
            x = (x - rest) // 10
            res = rest + res * 10

        if res > 2 ** 31 - 1:
            return 0

        return -res if negative else res

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
