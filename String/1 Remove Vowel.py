'''
REMOVE VOWELS FROM STRING
'''

class Solution:
	def removeVowels(self, S):
	    vowels = ['a','e','i','o','u']
	    result = ""
		for char in s:
		    if char.lower() not in vowels:
		        result += char
		return result
        
        
'''
DEFANGING AN IP ADDRESS

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"       
'''
      
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = address.replace(".","[.]")
        return result
        
'''
FINAL VALUE OF VARIABLE AFTER PERFORMING OPERATIONS

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.      
'''        
                
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret = 0
        for op in operations:
            if op == "--X" or op == "X--":
                ret -= 1
            else:
                ret += 1
        return ret
