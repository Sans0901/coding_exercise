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
        