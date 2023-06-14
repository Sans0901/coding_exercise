class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = []
        for i in range(len(nums)):
            if nums[i] not in output:
                output.append(nums[i])
        
        for i in range(len(output)):
            nums[i] = output[i]
        
        return len(output)
      
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setnums = set(nums)
        nums.clear()
        nums.extend(sorted(setnums))
        k = len(nums)
        return k

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:      
        n = len(nums)
        if n <= 1:
            return n
        
        j = 1  # index to track the unique elements
        
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        
        return j

#Here we are returning size of array after removing duplicates.

'''

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            print(nums)
            
            
            
            
'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Used binary search algorithm
'''
            
            
            
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid +1 

        return left