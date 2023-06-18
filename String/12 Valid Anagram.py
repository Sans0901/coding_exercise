'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unicode_values1 = sorted([ord(char) for char in s])
        unicode_values2 = sorted([ord(char) for char in t])
        if len(unicode_values1) == len(unicode_values2):
            if unicode_values1 == unicode_values2:
                return True
        return False
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        return dict1 == dict2
        
class Solution(object):
    def isAnagram(self, s, t):
        # In case of different length of thpse two strings...
        if len(s) != len(t):
            return False
        for idx in set(s):
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
            # If they are different, return false...
            if s.count(idx) != t.count(idx):
                return False
        return True     # Otherwise, return true...
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter