'''
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 == str2+str1:
            return str1[:math.gcd(len(str1), len(str2))]
        else:
            return ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the length of the GCD string
        gcd_len = self.find_gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
    
    def find_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a