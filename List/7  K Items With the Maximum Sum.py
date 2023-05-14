'''
Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
Output: 2
Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. 
We take 2 items with 1 written on them and get a sum in a total of 2.
It can be proven that 2 is the maximum possible sum.

'''


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = []
        for i in range(numOnes):
            nums.append(1)
        for i in range(numZeros):
            nums.append(0)
        for i in range(numNegOnes):
            nums.append(-1)
        
        nums.sort(reverse=True)
        
        return sum(nums[:k])