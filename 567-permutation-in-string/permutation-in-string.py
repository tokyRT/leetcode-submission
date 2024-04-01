class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        right=len(s1)-1
        for i in range(len(s2)-len(s1)+1):
            if sorted(s2[i:right+1])==sorted(s1):return True
            right+=1
        return False
