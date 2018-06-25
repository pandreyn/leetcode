"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # if numRows < 3:
        #     return s

        n = len(s)
        l, j = 0, 0 
        isZig = False
        table = [[0 for x in range(n)] for y in range(numRows)]  
        steps = numRows - 2

        while l < n:
            if isZig:
                for i in range(steps, 0, -1):
                    if l < n:
                        table[i][j] = s[l]
                    else:
                        break
                    l += 1
                    j += 1
                isZig = False
            else:
                for i in range(numRows):
                    if l < n:
                        table[i][j] = s[l]
                    else:
                        break
                    l += 1
                j += 1                        
                isZig = True
        
        result = ''
        for i in range(numRows):
            for j in range(n):
                if table[i][j] != 0:
                    result += table[i][j]

        return result



# print(Solution().convert("PAYPALISHIRING", 4))
# print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("ABC", 2))