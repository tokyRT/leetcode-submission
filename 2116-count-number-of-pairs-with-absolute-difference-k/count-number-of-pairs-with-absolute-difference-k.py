class Solution(object):
    def countKDifference(self, nums, k):
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    ans+=1
        return ans
        