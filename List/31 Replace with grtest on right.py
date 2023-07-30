'''
Find lucky number

Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

'''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_number = -1
        for num in arr:
            if arr.count(num) == num:
                lucky_number = max(lucky_number, num)  
        return lucky_number
        
'''        
Replace Elements with Greatest Element on Right Side

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.     
'''        
        
        
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        #Method 1:
        
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = curr_max
            if temp > curr_max:
                curr_max = temp
        return arr
        
        #Method 2:
        
        n = len(arr)
        max_val = -1  # Initialize the maximum value as -1

        # Traverse the array in reverse order
        for i in range(n - 1, -1, -1):
            temp = arr[i]  # Store the current element to update the array with the greatest value on the right
            arr[i] = max_val  # Replace the current element with the greatest value on the right
            max_val = max(max_val, temp)  # Update the maximum value encountered so far

        return arr
        
        #Method 3: But it having complexity as n2
        
        output = []
        op = [-1] * len(arr)
        for i in range(len(arr) - 1):
            if len(arr[i+1:]) > 0:  
                op[i] = max(arr[i+1:]) 
            else: 
                op[i] = -1 

            output.append(op[i])
        output.append(-1)
        return output
        