'''
11. Container With Most Water
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        right = n - 1
        left = 0 
        op = []

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            res = width * min_height
            op.append(res)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max(op)
            

'''
RICHEST CUSTOMER WEALTH

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        op = []
        for my_list in accounts:
            wealth = sum(my_list)
            op.append(wealth)
        return max(op)

'''
1365. How Many Numbers Are Smaller Than the Current Number

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = []
        for i in range(len(nums)):
            ct = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    ct += 1
            count.append(ct)
        return count