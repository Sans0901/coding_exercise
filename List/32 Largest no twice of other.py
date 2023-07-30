'''
Largest Number At Least Twice of Others

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

'''
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x = max(nums)
        dominant_idx = -1
        
        for i in range(len(nums)):
            if nums[i] != x and (2 * nums[i]) > x:
                return -1  # Early return as the condition is not met for a dominant index
            elif nums[i] == x:
                dominant_idx = i
                
        return dominant_idx