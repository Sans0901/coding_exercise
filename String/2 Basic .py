'''
JEWELS AND STONES

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for char in stones:
            if char in jewels :
                res += 1
        return res
        
        
'''
MAXIMUM NUMBER OF WORDS FOUND IN SENTENCES

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation: 
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.

'''   
           
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result, output = [], []
        for i in range(len(sentences)):
            result.append(sentences[i].split())
            output.append(len(result[i]))
        return max(output)
        
'''
GOAL PARSER INTERPRETATION

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

'''
class Solution:
    def interpret(self, command: str) -> str:
        new_string = command.replace("()","o")
        new_string1 = new_string.replace("(al)","al")
        return new_string1