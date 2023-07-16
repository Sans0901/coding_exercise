'''
SORT EVEN AND ODD INDICES INDEPENDENTLY

Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation: 
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
'''
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd_idx = []
        even_idx = []
        for i in range(n):
            if i%2 == 0:
                even_idx.append(nums[i])
            else:
                odd_idx.append(nums[i])
        odd_idx.sort(reverse=True)
        even_idx.sort()
        #print(odd_idx)
        #print(even_idx)
        nums.clear()
        for i in range(n):
            if i%2 == 0:
                nums.append(even_idx[i//2])
            else:
                nums.append(odd_idx[i//2])
        return nums
        
'''
905. Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]

'''
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_idx = []
        even_idx = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even_idx.append(nums[i])
            else:
                odd_idx.append(nums[i])
        print(even_idx)
        print(odd_idx)
        even_idx.extend(odd_idx)
        return even_idx
        
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        temp = 0
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i], nums[temp] = nums[temp], nums[i]
                temp += 1
        return nums

'''
922. Sort Array By Parity II

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_ele = []
        odd_ele = []
        for i in range(n):
            if nums[i] % 2 == 0:
                even_ele.append(nums[i])
            else:
                odd_ele.append(nums[i])
        even_ele.sort(reverse=True)
        odd_ele.sort(reverse=True)
        #print(even_ele)
        #print(odd_ele)
        nums.clear()
        for i in range(n):
            if i%2==0:
                nums.append(even_ele[i//2])
            else:
                nums.append(odd_ele[i//2])
        return nums
        
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_ele = []
        odd_ele = []
        for i in range(n):
            if nums[i] % 2 == 0:
                even_ele.append(nums[i])
            else:
                odd_ele.append(nums[i])
        even_ele.sort(reverse=True)
        odd_ele.sort(reverse=True)
        #print(even_ele)
        #print(odd_ele)
        nums.clear()
        for i in range(n):
            if i%2==0:
                nums.append(even_ele[i//2])
            else:
                nums.append(odd_ele[i//2])
        return nums

'''
2149. Rearrange Array Elements by Sign

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
'''
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        for i in range(n):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        '''
        print(pos)
        print(neg)
        pos.sort(reverse=True)
        neg.sort(reverse=True)
        '''
        nums.clear()
        for i in range(n):
            if i%2 == 0:
                nums.append(pos[i//2])
            else:
                nums.append(neg[i//2])
        return nums