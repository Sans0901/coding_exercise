'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = 0
        for digit in digits:
            output = output * 10 + digit

        output = output + 1
        output_digits = []
        while output > 0:
            output_digits.insert(0, output % 10)
            output = output // 10
        return output_digits