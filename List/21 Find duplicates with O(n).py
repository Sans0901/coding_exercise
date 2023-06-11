'''
FIND ALL DUPLICATES IN AN ARRAY

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums.count(num) > 1 and num not in result:
                result.append(num)
        return result

# In this solution used o(n^2) but we can performed it in o(n)
#Optimized solution

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            n = abs(n)
            if nums[n-1] > 0:
                nums[n-1] *= -1
            else:
                result.append(n)
        return result
