def pivot(nums):
    left, right = 0, len(nums)-1
    ans=nums[0]
    pivot=0
    while left <= right:
        mid = (left+right)//2
        if nums[left] <= nums[mid]:
            if nums[left] < ans: pivot=left
            ans = min(ans, nums[left])
            left  = mid+1
        else:
            if nums[mid] < ans: pivot=mid
            ans=min(ans, nums[mid])
            right=mid-1
    return pivot
class Solution(object):
    def search(self, nums, target):
        p=pivot(nums)
        ans=-1
        if p > 0 and (nums[0] <= target <= nums[p-1]):
            left=0
            right=p-1
        else:
            left=p
            right=len(nums)-1
        print(left, right)
        while left <= right:
            mid=(left+right)//2
            if target == nums[mid]:
                ans=mid
                break
            elif target<nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return ans
        