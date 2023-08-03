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