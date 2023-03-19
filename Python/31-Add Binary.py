class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num=int(a,2)
        num2=int(b,2)
        res=num+num2
        return bin(res)[2:]
'''
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
