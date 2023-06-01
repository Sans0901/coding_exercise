'''
SHUFFLE STRING

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
'''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        shuffled = [""] * n

        for i in range(n):
            shuffled[indices[i]] = s[i]

        return "".join(shuffled)
        
'''
CHECK IF TWO STRING ARRAYS ARE EQUIVALENT

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false       
'''
        
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
        
        
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:       
    str1 = ''.join(word1)
        str2 = ''.join(word2)
        if str1 == str2:
            return True
        else:
            return False
