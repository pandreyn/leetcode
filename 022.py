"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solution = []
        def recursion(n, str):
            if len(str) == 2 * n:
                solution.append(str)
            else:
                opened, closed = 0, 0
                for i in range(len(str)):
                    if str[i] == '(':
                        opened += 1
                    if str[i] == ')':
                        closed += 1
                
                if opened == closed:
                    recursion(n, str + "(")
                elif closed < opened:
                    if opened < n:
                        recursion(n, str + "(")
                    recursion(n, str + ")")

        recursion(n, "")
        return solution
        
print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(0))
