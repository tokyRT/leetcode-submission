class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        ans=nums[0]
        while left <= right:
            mid = (left+right)//2
            if nums[left] <= nums[mid]:
                ans = min(ans, nums[left])
                left  = mid+1
            else:
                ans=min(ans, nums[mid])
                right=mid-1
        return ans
        