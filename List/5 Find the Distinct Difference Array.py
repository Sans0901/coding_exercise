'''
You are given a 0-indexed array nums of length n.
The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct
elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].
Return the distinct difference array of nums.


Input: nums = [1,2,3,4,5]
Output: [-3,-1,1,3,5]

'''

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            preffix_count = len(set(nums[:i+1]))
            suffix_count = len(set(nums[i+1:]))
            output.append(preffix_count-suffix_count)
        return output