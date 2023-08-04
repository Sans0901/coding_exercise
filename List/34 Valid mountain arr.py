'''
941. Valid Mountain Array

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true

'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        mx = arr.index(max(arr))
        if n > 3:
            return False
        if mx == 0 or mx == n-1:
            return False
        for i in range(mx):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(mx,n-1):
            if arr[i] <= arr[i+1]:
                return False
        return True
        
        
'''
1608. Special Array With X Elements Greater Than or Equal X

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        for x in range(n + 1):
            count = sum(1 for num in nums if num >= x)
            if count == x:
                return x
        return -1