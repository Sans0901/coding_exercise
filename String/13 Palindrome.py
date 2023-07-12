'''
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^A-Za-z0-9]', '', s)
        joined_string = ''.join(cleaned_string.split())
        reversed_string = joined_string[::-1]
        #print(joined_string)
        #print(reversed_string)
        if joined_string.lower() == reversed_string.lower():
            return True
        return False
        
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))

        reversed_string = s[::-1]
        return reversed_string == s
     
        print(s)
        
"""
1. Convert to lowercase, remove all alphaneumeric characters
2. Reverse the string, and compare it to the original string

"""

'''
FIND THE DIFFERENCE
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
                t_count = Counter(t)
                
                for char, count in t_count.items():
                    if count > s_count[char]:
                        return char
                        
                        
        for i in t:
            if t.count(i) != s.count(i) or i not in s:
                return i