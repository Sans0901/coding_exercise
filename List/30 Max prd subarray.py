'''
MAXIMUM PRODUCT SUBARRAY 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        overall_max_product = nums[0]

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Calculate the new maximum and minimum product considering the current element
            curr = nums[i]
            temp_max = max(curr, max_product * curr, min_product * curr)
            temp_min = min(curr, max_product * curr, min_product * curr)

            # Update the overall maximum product if necessary
            overall_max_product = max(overall_max_product, temp_max)

            # Update the variables for the next iteration
            max_product = temp_max
            min_product = temp_min

        return overall_max_product

'''
238. Product of Array Except Self

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
''' 
  
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1]
        
        rightprd = 1

        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * rightprd
            rightprd = rightprd * nums[i]

        return ans
        
nums = [1,2,3,4]
ans = [1,1,1,1]
ans = [1,1,2,6] Started from 1st element
rightprd = [24,12,8,6]
op = [24,12,8,6]
We have taken new list ans whose length is same as nums and initialize it with 1
traversing from left to right ans we are considering ans[1] = multiplication of previous index elements of ans and nums.
Then taken new var rightprd and initializes with 1. Again upadting the ans list for getting required outcome.
rightprd = ans of last element will update last element as 6 

