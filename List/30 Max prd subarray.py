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