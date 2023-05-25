'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num1 in nums1:
            flag = False
            for num2 in nums2:
                if num1 == num2:
                    flag = True
                elif flag and num2 > num1:
                    output.append(num2)
                    break
            else:
                output.append(-1)

        return output
'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its
 next greater number. If it doesn't exist, return -1 for this number.

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.     
     
'''     
        
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Initialize a stack to keep track of indices of elements we haven't found a next greater element for
        stack = []
        
        # Initialize the result list to contain all -1s (assuming we won't find any next greater element)
        result = [-1] * len(nums)
        
        # Loop through the array twice (to handle circularity) and process each element
        for _ in range(2):
            for i in range(len(nums)):
                # Pop elements off the stack if they are less than the current element and update their result
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]
                
                # Add the current index to the stack
                stack.append(i)
        
        # Return the result list
        return result