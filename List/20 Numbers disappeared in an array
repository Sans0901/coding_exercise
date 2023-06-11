'''
FIND ALL NUMBERS DISAPPEARED IN AN ARRAY

ay nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        result = []
        
        for i in range(1, n+1):
            if i not in num_set:
                result.append(i)
        
        return result