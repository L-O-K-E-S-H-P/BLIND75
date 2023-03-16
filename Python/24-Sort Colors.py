'''Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        To solve this problem, we can use the Dutch National Flag algorithm.
        """
        l=0
        m=0
        h=len(nums)-1
        while(m<=h):
            if(nums[m]==0):
                nums[l],nums[m]=nums[m],nums[l]
                l=l+1
                m=m+1
            elif(nums[m]==1):
                m=m+1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h=h-1
        return nums
