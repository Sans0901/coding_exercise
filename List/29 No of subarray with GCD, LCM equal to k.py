'''
Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
'''
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b:
                a,b = b,a % b
            return a
        count = 0
        n = len(nums)
        for i in range(n):
            g = nums[i]
            for j in range(i,n):
                g = gcd(g,nums[j])
                if g == k:
                    count += 1
        return count

'''
Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
'''
   
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def gcd(a,b):
            while b:
                a,b = b,a % b
            return a
        def lcm(a, b):
            return abs(a * b) // math.gcd(a, b)
        
        n = len(nums)
        count = 0
        
        for i in range(n):
            l = nums[i]
            if l == k:
                count += 1
                
            for j in range(i + 1, n):
                l = lcm(l, nums[j])
                if l == k:
                    count += 1
        
        return count