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