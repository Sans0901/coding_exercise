class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = []
        for i in range(len(nums)):
            if nums[i] not in output:
                output.append(nums[i])
        
        for i in range(len(output)):
            nums[i] = output[i]
        
        return len(output)









#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            print(nums)
            