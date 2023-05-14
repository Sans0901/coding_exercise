'''
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

'''

class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0]
        rightSum = [0]*n
        output = []
        for i in range(n-1):
            leftSum.append(leftSum[i]+nums[i])
            rightSum[n-i-2] = rightSum[n-i-1]+nums[n-i-1]
            
        for i in range(n):
            output.append(abs(leftSum[i]-rightSum[i]))
        return output
