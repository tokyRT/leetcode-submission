class Solution(object):
    def findMin(self, nums):
        ans=nums[0]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]: ans=nums[i+1]
        return ans
        