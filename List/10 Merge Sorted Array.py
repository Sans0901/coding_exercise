'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #1
        #Do not return anything, modify nums1 in-place instead.
        
        i=0
        for x in range(len(nums1)):
            if i>=n:                   # checks whether all elements from num2 have been inserted into nums1
                break
            if nums1[x]==0:            # nums1 any element is 0 then it will proceed with nums2 element.
                nums1[x]=nums2[i]
                i+=1           
        nums1.sort()
        #2                             # this method directly deletes non required elememts from nums1 and then will be merge with nums2 and then sort it.
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()
        #3
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else :
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        while n>0:                      #This loop is bcoz if both contain single element and one of them is zero
            nums1[m+n-1] = nums2[n-1]
            n -= 1