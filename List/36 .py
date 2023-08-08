'''
1389. Create Target Array in the Given Order

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

'''
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

'''
1720. Decode XORed Array

Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
'''       
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        #a ^ i = b
        #    a = b ^ i
        op = [first]
        for i in encoded:
            op.append(op[-1] ^ i)
        return op 
            
'''            
2535. Difference Between Element Sum and Digit Sum of an Array
Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.                    
'''         
            
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        string_list = [str(num) for num in nums]
        result_list = []

        for item in string_list:
            for char in item:
                result_list.append(int(char))
        result_list = sum(result_list)
        return abs(s-result_list)

#Optimzed Solution

        es = sum(nums)
        dg=0
        for x in nums:
            while x>0:
                dg+=(x%10)
                x=x//10
        return abs(es-dg)