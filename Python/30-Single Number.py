class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq_num=0
        '''Concept of XOR:
        XOR of zero and some bit returns that bit i.e. x^0 = x...
        XOR of two same bits returns 0 i.e. x^x = 0...
        And, x^y^x = (x^x)^y = 0^y = y...
        XOR all bits together to find the unique number.'''
        for i in nums:
            uniq_num^=i
        return uniq_num
'''
Example 1:

Input: nums = [2,2,1]
Output: 1
'''
