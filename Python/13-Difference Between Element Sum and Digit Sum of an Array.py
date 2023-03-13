'''You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|
'''
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        c=sum(nums)
        total=0
        for n in nums:
            total+=sum(int(digit) for digit in str(n))
        return abs(c-total)
