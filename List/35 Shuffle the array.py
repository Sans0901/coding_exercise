'''
SHUFFLE THE ARRAY 
Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k = len(nums)
        odd = []
        even = []
        for i in range(n):
            odd.append(nums[i])
        #print(odd)
        for i in range(n,k):
            even.append(nums[i])
        #print(even)
        nums.clear()
        for i in range(k):
            if i%2 == 1:
                nums.append(even[i//2])
            else:
                nums.append(odd[i//2])
        return nums

'''
NUMBER OF GOOD PAIRS

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        op = []
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    op.append((i,j))
                    count += 1
        return count
        
'''
1431. Kids With the Greatest Number of Candies

Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_candies = max(candies)  
        bool_list = [candy + extraCandies >= max_candies for candy in candies]
        return bool_list