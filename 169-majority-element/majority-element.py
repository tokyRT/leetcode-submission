class Solution(object):
    def majorityElement(self, nums):
        count = dict()
        for elem in nums:
            if elem in count.keys(): count[elem] += 1
            else: count[elem] = 1
        k=0
        m=0
        for key, value in count.items():
            if value>m:
                m=value
                k=key
        return k
        