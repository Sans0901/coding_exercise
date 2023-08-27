'''
424. Longest Repeating Character Replacement

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        charCount = {}  # Dictionary to store character counts
        i, j = 0, 0
        maxCount = 0  # Track the maximum character count in the window
        ans = 0
        
        while j < n:
            charCount[s[j]] = charCount.get(s[j], 0) + 1  # Update character count
            
            maxCount = max(maxCount, charCount[s[j]])  # Update max character count
            
            # If the number of characters that need replacement exceeds k, move the window's left boundary
            while (j - i + 1 - maxCount) > k:
                charCount[s[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)  # Update ans with the current window length
            j += 1  # Move the window to the right
        
        return ans