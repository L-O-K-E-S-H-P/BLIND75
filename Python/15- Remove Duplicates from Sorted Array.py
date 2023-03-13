'''Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i=1
        prev=nums[0]
        while(i<len(nums)):
            if(nums[i]==prev):
                nums.pop(i)
            else:
                prev=nums[i]
                i+=1
        return len(nums)
