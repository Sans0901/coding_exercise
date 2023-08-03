'''
2148. Count Elements With Strictly Smaller and Greater Elements

Example 1:

Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.
Example 2:

Input: nums = [-3,3,3,90]
Output: 2
Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.
'''
class Solution:
    def countElements(self, nums: List[int]) -> int:
        mi = min(nums)
        mx = max(nums)
        count = 0
        for i in range(len(nums)):
            if mi < nums[i] < mx:
                count += 1
        return count
        
'''
744. Find Smallest Letter Greater Than Target

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]
        return min(letters)
           