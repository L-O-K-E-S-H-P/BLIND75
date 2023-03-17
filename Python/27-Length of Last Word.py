'''
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=s.split()[-1]
        return len(c)
        
    
