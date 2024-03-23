import math
def combinaisons(n, k):
  return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
class Solution(object):
    def numIdenticalPairs(self, nums):
        c={}
        for i in nums:
            if i in c.keys():
                c[i]+=1
            else: c[i]=1
        r=0
        for k, v in c.items():
            if v>1: r+=combinaisons(v,2)
        return r