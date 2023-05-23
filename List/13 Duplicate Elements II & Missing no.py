'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
(k = index(first occurence) - index(second occurence))
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Map = {}
        for i in range(len(nums)):
            current = nums[i]
            if current in Map and i-Map[current] <=k:
                return True
            else:
                Map[current] = i
        return False
        
        
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2

        actual_sum = sum(nums)                                      #actual sum of the elements in the array
        missing_number = expected_sum - actual_sum                  #missing number is the difference between the expected and actual sum

        return missing_number
                