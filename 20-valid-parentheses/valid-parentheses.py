class Solution(object):
    def isValid(self, s):
        v=s
        while True:
            if v=="": return True

            tmp=v
            v=v.replace("()", "")
            v=v.replace("[]", "") 
            v=v.replace("{}", "")
            
            if v==tmp: return False
        