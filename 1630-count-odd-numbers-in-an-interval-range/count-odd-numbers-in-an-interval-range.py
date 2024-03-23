class Solution:
    def countOdds(self, low: int, high: int) -> int:
        r=0
        low = low + 1 if low%2==0 else low
        # for i in range(low, high+1, 2):
        #     if i %2==1: r+=1
        return (high - low)//2 + 1