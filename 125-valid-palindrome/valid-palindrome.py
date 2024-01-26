import math
class Solution(object):
    def isPalindrome(self, s):
        s="".join(l.lower() for l in s if l.isalnum())
        print(s)
        right=len(s)-1
        for left in range(int(math.ceil(len(s)/2))):
            if s[left] != s[right]: return False
            right-=1
        return True
        