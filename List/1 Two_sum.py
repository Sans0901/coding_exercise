def twoSum(nums: list[int], target: int) -> list[int]:
   output = []
   for i in nums:
        for j in nums:
            if i + j == target and nums.index(i) != nums.index(j):
                output.append(nums.index(i))
                output.append(nums.index(j))
                return output

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))

'''
1.Did with help of two for loops with time complexity o(n^2)
2.It can be done using dictionary too with time complexity o(n)
'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_value = {}

        for index, value in enumerate(nums):
            required_no = target - value

            if required_no in seen_value:
                return(index, seen_value[required_no])
            else:
                seen_value[value] = index
