'''
2413. Smallest Even Multiple

Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 
Example 1:

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
'''

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return 2 * n
            
'''          
    Find Greatest Common Divisor of Array
    Example 1:

    Input: nums = [2,5,6,9,10]
    Output: 2
    Explanation:
    The smallest number in nums is 2.
    The largest number in nums is 10.
    The greatest common divisor of 2 and 10 is 2.
    Example 2:

    Input: nums = [7,5,6,8,3]
    Output: 1
    
        
'''
         
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n1 = min(nums)
        n2 = max(nums)
        gcd = math.gcd(n1, n2)
        return gcd
        
'''
Three Divisors

Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
'''
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1,n+1):
            if n%i == 0:
                count += 1
        if count == 3:
            return True
        else:
            return False