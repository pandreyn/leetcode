"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        prefix =""
        
        for i in range(len(strs[0])):
            eq = True
            for j in range(1, len(strs)):
                if (i < len(strs[j]) and strs[0][i] != strs[j][i]) or i >= len(strs[j]):
                    eq = False
                    break

            if eq:
                prefix = prefix + strs[0][i]
            else: 
                break

        return prefix


print(Solution().longestCommonPrefix(["aa","a"]))
print(Solution().longestCommonPrefix([""]))
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
