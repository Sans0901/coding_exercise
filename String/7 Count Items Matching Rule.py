'''
COUNT ITEMS MATCHING A RULE
Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
Example 2:

Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"].
Note that the item ["computer","silver","phone"] does not match.
'''

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                count += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                count += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                count += 1
        return count
