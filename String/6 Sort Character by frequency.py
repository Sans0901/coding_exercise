'''
SORT CHARACTERS BY FREQUENCY

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

'''

class Solution:
    def frequencySort(self, s: str) -> str:
        ch_dict = {}
        for char in s:
            if char in ch_dict:
                ch_dict[char] += 1
            else:
                ch_dict[char] = 1
        
        sort_dict = dict(sorted(ch_dict.items(), key=lambda item: item[1], reverse = True))
        key_string = ''.join(char * freq for char, freq in sort_dict.items())
        return key_string
