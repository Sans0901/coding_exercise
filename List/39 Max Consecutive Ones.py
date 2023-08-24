'''
Max Consecutive Ones

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        op = []
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                op.append(count)
                count = 0
        op.append(count)  # Account for the last sequence of ones
        return max(op)
        
'''
Max Consecutive Ones III

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ZeroCount, i, j = 0, 0, 0
        ans = 0  # Initialize ans with 0
        while j < n:
            if nums[j] == 0:
                ZeroCount += 1
            while ZeroCount > k:
                if nums[i] == 0:
                    ZeroCount -= 1
                i += 1
            ans = max(ans, j - i + 1)  # Update ans with the current window length
            j += 1  # Move the window to the right
        return ans