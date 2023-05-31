'''
SPLIT A STRING IN BALANCED STRINGS
Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0  # count of balanced substrings
        balance = 0  # balance of 'L' and 'R' characters

        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count
        
        
        
# Optimized Solution

        output = 0
        count = 0
        for c in s:
            count = count + 1 if c == 'R' else count - 1
            if count == 0:
                output += 1
        return output