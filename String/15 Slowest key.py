'''
SLOWEST KEY 

Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"
Explanation: The keypresses were as follows:
Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
'c' is lexicographically larger than 'b', so the answer is 'c'.
'''
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        char_list = list(keysPressed)
        output = []
        output.append(releaseTimes[0])
        n = len(releaseTimes)
        for i in range(1,n):
            op = releaseTimes[i]-releaseTimes[i-1]
            output.append(op)
        #return output
        #print(output)
        max_indexes = [i for i, value in enumerate(output) if value == max(output)]
        #print(max_indexes)
        result = [keysPressed[i] for i in max_indexes]
        #print(result)
        return(max(result))

