def isPal(s):
    return s[::-1]==s
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s[::-1]==s:
            return 1
        if len(s)==0:
            return 0
        
        return 2
        