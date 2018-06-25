"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution:
    def __init__(self, *args, **kwargs):
        self.d = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
            
        combinations = []

        if (len(digits) < 1):
            return combinations

        def recurse(rest_of_the_word, path_so_far):
            if not rest_of_the_word:
                combinations.append(path_so_far)
                return

            first, rest = rest_of_the_word[0], rest_of_the_word[1:]
            letters = self.d[first]

            for letter in letters:
                recurse(rest, path_so_far + letter)

        recurse(digits, "")
        return combinations


#print(Solution().letterCombinations(""))
#print(Solution().letterCombinations("2378"))
print(Solution().letterCombinations("234"))
