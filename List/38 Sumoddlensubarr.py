'''
1588. Sum of All Odd Length Subarrays

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        presum = [0]*(n+1)

        for i in range(n):
            presum[i+1] += presum[i] + arr[i]

        for i in range(n):
            for j in range(i+1,n+1):
                if(j-i)%2:
                    ans += presum[j] - presum[i]
        return ans
        
'''
2367. Number of Arithmetic Triplets

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
'''
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
        return count
       
# Optimized solution

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        hs = set(nums) 
        ct = 0
        
        for i in nums:
            if i - diff in hs and i + diff in hs:
                ct += 1
        return ct