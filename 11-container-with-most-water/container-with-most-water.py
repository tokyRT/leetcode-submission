class Solution(object):
    def maxArea(self, height):
        ans=0
        left, right = 0, len(height)-1
        while left <= right:
            area = min(height[left], height[right]) * (right-left)
            ans = max(ans, area)
            if height[right]<=height[left]:
                right -= 1
            else:
                left += 1

        return ans