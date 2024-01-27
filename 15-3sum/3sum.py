class Solution(object):
    def threeSum(self, nums):
        triplets=set()
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            remain=-nums[i]
            left=i+1
            right=n-1
            while left < right:
                if nums[left]+nums[right] < remain: left+=1
                elif nums[left]+nums[right] > remain: right -= 1
                else:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left+=1
                    right-=1
        return list(triplets)

        