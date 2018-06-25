class Solution:
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s is None or s == s[::-1]:
        	return s
        maxLen = 1
        start = 0
        for i in range(1,len(s)):
        	if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
        		start = i - maxLen - 1
        		maxLen += 2
        		continue

        	if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
        		start = i - maxLen
        		maxLen += 1
        return s[start:start+maxLen]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s is None or s == s[::-1]:
        	return s

        n = len(s)
        table = [[0 for x in range(n)] for y in range(n)] 
        maxLength = 1

        for i in range(n):
            table[i][i] = True

        # check for sub-string of length 2.
        start = 0
        for i in range(n - 1):
            if (s[i] == s[i + 1]) :
                table[i][i + 1] = True
                start = i
                maxLength = 2

        # Check for lengths greater than 2. 
        # k is length of substring
        for k in range(3, n + 1):
            # Fix the starting index
            for i in range(n - k + 1):
                
                # Get the ending index of 
                # substring from starting 
                # index i and length k
                j = i + k - 1
        
                # checking for sub-string from
                # ith index to jth index iff 
                # st[i+1] to st[(j-1)] is a 
                # palindrome
                if (table[i + 1][j - 1] and s[i] == s[j]) :
                    table[i][j] = True
        
                    if (k > maxLength) :
                        start = i
                        maxLength = k

        return s[start:start + maxLength]

   
#print(Solution().checkPalindrome("baab"))
# print(Solution().longestPalindrome(None))
# print(Solution().longestPalindrome(""))

print(Solution().longestPalindrome("caba"))
print(Solution().longestPalindrome("adam"))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
