'''
LONGEST COMMON PREFIX

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        
        return shortest
        
'''
PALINDROME

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        return y == y[::-1]


        
        reversed_str = str(x)[::-1]
        reversed_digits_only = "".join(char for char in reversed_str if char.isdigit())
        yz = int(reversed_digits_only)
        if yz == x:
            return True
        else:
            return False
        