'''Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 Input: x = 2.00000, n = 10
Output: 1024.00000
'''
import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        c=math.pow(x,n)
        return c
