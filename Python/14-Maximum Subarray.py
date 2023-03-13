'''Given an integer array nums, find the subarray with the largest sum, and return its sum.
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''
class Solution:
  def maxSubArray(self,nums:List[int])->int:
    max=nums[0]
    c=0
    for i in nums:
      c=c+i
      if max<c:
        max=c
      if c<0:
        c=0
    return max
