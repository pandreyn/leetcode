class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        

        start = 0
        maxlen = 1
        dict = {}
        dict[s[0]] = 0

        for i in range(1, len(s)):
            c = s[i]
            if c in dict and dict[c] >= start:
                start = dict[c] + 1
            
            dict[c] = i
            maxlen = max(maxlen, i - start + 1)

        return maxlen



print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("aab"))
print(Solution().lengthOfLongestSubstring("dvdf"))