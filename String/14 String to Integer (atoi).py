class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()										# Remove whitespace

        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1						# Check if the number is negative or positive
															# Skip the sign character if present
        if s[0] in ('-', '+'):
            s = s[1:]

        num = 0												# Read digits until the next non-digit character or the end of the string
        i = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
			
        num *= sign											# Apply the sign to the number
        num = max(min(num, 2**31 - 1), -2**31)				# Clamp the number within the 32-bit signed integer range
        return num
        
        
'''
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''     
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1 