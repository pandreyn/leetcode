"""
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
class Solution:
    def __init__(self, *args, **kwargs):
        self.open = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        self.close = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        if len(s) < 2:
            return False

        stack = []
        for i in range(len(s)):
            p = s[i]
            if p in self.open:
                stack.append(s[i])
            
            if p in self.close:
                if len(stack) == 0:
                    return False
                c = stack.pop()
                if self.close[p] != c:
                    return False

        if len(stack) > 0:
            return False
            
        return True
                

        
print(Solution().isValid("["))
print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("([)]"))
print(Solution().isValid("{[]}"))