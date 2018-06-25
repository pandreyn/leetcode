"""
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        pLen = len(p)
        sLen = len(s)

        if pLen == 0:
            return sLen == 0
        
        # p's Length 1 is special case
        if pLen == 1 or p[1] != "*":
            if sLen < 1 or (p[0] != "." and s[0] != p[0]):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            i = -1
            while(i < sLen and (i < 0 or p[0] == "." or p[0] == s[i])):
                if (self.isMatch(s[i+1:], p[2:])):
                    return True
                i += 1
            return False

                

print(Solution().isMatch("aa", "a")) #false
print(Solution().isMatch("aa", "a*")) #true
print(Solution().isMatch("ab", ".*")) #true
print(Solution().isMatch("aab", "c*a*b")) #true
print(Solution().isMatch("mississippi", "mis*is*p*.")) #false
