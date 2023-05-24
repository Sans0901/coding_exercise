'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []  # Initialize answer as an empty list
        diff_nums1 = list(set(nums1) - set(nums2))  # Calculate the difference between nums1 and nums2
        diff_nums2 = list(set(nums2) - set(nums1))  # Calculate the difference between nums2 and nums1

        answer.append(diff_nums1)
        answer.append(diff_nums2)

        return answer
        '''
        answer = [[]]  # Initialize answer as an empty list
        for ele in nums1:
            if ele not in nums2:  # Check if ele is not in nums2
                answer.append([ele])


        for ele in nums2:
            if ele not in nums1:  # Check if ele is not in nums1
                 answer.append([ele])

        return answer
        '''