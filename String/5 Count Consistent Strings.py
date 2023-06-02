'''
COUNT THE NUMBER OF CONSISTENT STRINGS

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count
        
# OPTIMIZED SOLUTION

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            no_extra = True
            for ch in word:
                if ch not in allowed:
                    no_extra = False
                    break
            if no_extra:
                count += 1
        return count
        
        
'''
COUNT PAIRS OF SIMILAR STRINGS

Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 

'''
class Solution:
  def similarPairs(self, words: List[str]) -> int:
    return sum(set(words[i]) == set(words[j])
               for i in range(len(words))
               for j in range(i + 1, len(words)))