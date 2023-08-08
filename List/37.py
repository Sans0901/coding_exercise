'''
2656. Maximum Sum With Exactly K Elements

Input: nums = [1,2,3,4,5], k = 3
Output: 18
Explanation: We need to choose exactly 3 elements from nums to maximize the sum.
For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
So, we will return 18.
It can be proven, that 18 is the maximum answer that we can achieve.
'''
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s = 0
        op = []
        n = len(nums)
        nums.sort()
        for i in range(k):
            s = nums[n-1]
            op.append(nums[n-1])
            nums[n-1] = nums[n-1] +1
        total = sum(op)
        return total
        
#Optimized Solution

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        max_score = 0

        for i in range(k):
            max_score += max_num
            max_num += 1
        return max_score