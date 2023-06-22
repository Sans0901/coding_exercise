'''
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        left = 0
        right = len(nums) - 1
        
        # Binary search to find the leftmost index
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left < len(nums) and nums[left] == target:
            output[0] = left
        
        left = 0
        right = len(nums) - 1
        
        # Binary search to find the rightmost index
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        if right >= 0 and nums[right] == target:
            output[1] = right
        
        return output